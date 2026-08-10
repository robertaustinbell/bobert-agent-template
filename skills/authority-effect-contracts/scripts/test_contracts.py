from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from contracts import (  # type: ignore[import-not-found]
    ContractError,
    check_authority_subset,
    validate_authority_manifest,
    validate_effect_receipt,
)


def authority(**updates):
    value = {
        "schema_version": "authority-manifest/v1",
        "manifest_id": "parent-1",
        "task_id": "inspect-report-1",
        "task": "Inspect a named repository and write one report",
        "may": ["inspect_repository", "write_named_artifact", "run_tests"],
        "must_not": ["push", "publish", "merge", "send_message", "spend_money"],
        "targets": ["/tmp/authority-contract-example"],
        "ask_before": ["scope_expansion", "new_external_effect"],
        "verification": ["artifact_hash_recorded", "tests_pass"],
        "stop_on": ["ambiguous_target", "partial_external_failure", "policy_change"],
        "valid_until": (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat(),
    }
    value.update(updates)
    return value


def receipt(**updates):
    value = {
        "schema_version": "external-effect-receipt/v1",
        "receipt_id": "receipt-1",
        "effect_status": "requested",
        "evidence_completeness": "unknown",
        "target": "/tmp/authority-contract-example/report.md",
        "operation": "write_named_artifact",
        "acting_surface": None,
        "observed_at": None,
        "verification_evidence": [],
        "sensitive_payload_retained": False,
    }
    value.update(updates)
    return value


class AuthorityContractTests(unittest.TestCase):
    def test_valid_manifest_is_accepted(self):
        validate_authority_manifest(authority())

    def test_unknown_field_is_rejected(self):
        with self.assertRaises(ContractError):
            validate_authority_manifest(authority(surprise=True))

    def test_child_cannot_expand_action_or_target(self):
        parent = authority()
        child = authority(
            manifest_id="child-1",
            may=["inspect_repository", "push"],
            must_not=["publish", "merge", "send_message", "spend_money"],
            targets=["/tmp/other"],
        )
        errors = check_authority_subset(parent, child)
        self.assertTrue(any("may" in error for error in errors))
        self.assertTrue(any("targets" in error for error in errors))

    def test_child_cannot_drop_parent_prohibition_or_approval_gate(self):
        parent = authority()
        child = authority(
            manifest_id="child-1",
            must_not=["publish"],
            ask_before=[],
        )
        errors = check_authority_subset(parent, child)
        self.assertTrue(any("must_not" in error for error in errors))
        self.assertTrue(any("ask_before" in error for error in errors))

    def test_child_may_narrow_authority(self):
        parent = authority()
        child = authority(
            manifest_id="child-1",
            may=["inspect_repository"],
            must_not=parent["must_not"] + ["write_named_artifact"],
            ask_before=parent["ask_before"] + ["write_named_artifact"],
            valid_until=parent["valid_until"],
        )
        self.assertEqual(check_authority_subset(parent, child), [])

    def test_child_cannot_change_task_identity(self):
        parent = authority()
        child = authority(manifest_id="child-task", task_id="different-task", task="Different prose")
        errors = check_authority_subset(parent, child)
        self.assertIn("child task_id differs from parent", errors)

    def test_child_cannot_outlive_parent(self):
        parent = authority(valid_until="2099-01-01T00:00:00+00:00")
        child = authority(manifest_id="child-late", valid_until="2099-01-02T00:00:00+00:00")
        self.assertIn("child valid_until exceeds parent", check_authority_subset(parent, child))

    def test_expired_authority_fails_dispatch_subset_check(self):
        parent = authority(valid_until="2020-01-01T00:00:00+00:00")
        child = authority(
            manifest_id="child-expired",
            valid_until="2020-01-01T00:00:00+00:00",
        )
        with self.assertRaises(ContractError):
            validate_authority_manifest(parent, require_active=True)
        errors = check_authority_subset(parent, child)
        self.assertIn("parent authority manifest is expired", errors)
        self.assertIn("child authority manifest is expired", errors)


class ReceiptContractTests(unittest.TestCase):
    def test_prepared_receipt_remains_non_execution(self):
        value = receipt(effect_status="prepared", evidence_completeness="complete")
        self.assertEqual(validate_effect_receipt(value)["effect_status"], "prepared")

    def test_attempted_receipt_requires_acting_surface_and_time(self):
        value = receipt(
            effect_status="attempted",
            evidence_completeness="unknown",
            acting_surface="local_filesystem",
            observed_at="2026-08-10T13:30:00+00:00",
        )
        self.assertEqual(validate_effect_receipt(value)["effect_status"], "attempted")
        value["acting_surface"] = None
        with self.assertRaises(ContractError):
            validate_effect_receipt(value)

    def test_observed_failure_is_not_success(self):
        value = receipt(
            effect_status="observed_failed",
            evidence_completeness="complete",
            acting_surface="local_filesystem",
            observed_at="2026-08-10T13:30:00+00:00",
        )
        self.assertEqual(validate_effect_receipt(value)["effect_status"], "observed_failed")

    def test_unknown_outcome_can_have_partial_evidence(self):
        value = receipt(effect_status="unknown", evidence_completeness="partial")
        accepted = validate_effect_receipt(value)
        self.assertEqual(accepted["effect_status"], "unknown")
        self.assertEqual(accepted["evidence_completeness"], "partial")

    def test_requested_receipt_is_not_success(self):
        validate_effect_receipt(receipt())

    def test_observed_success_requires_evidence(self):
        with self.assertRaises(ContractError):
            validate_effect_receipt(
                receipt(
                    effect_status="observed_succeeded",
                    evidence_completeness="complete",
                    acting_surface="filesystem",
                    observed_at=datetime.now(timezone.utc).isoformat(),
                )
            )

    def test_observed_success_rejects_unknown_evidence_kind(self):
        with self.assertRaises(ContractError):
            validate_effect_receipt(
                receipt(
                    effect_status="observed_succeeded",
                    evidence_completeness="complete",
                    acting_surface="filesystem",
                    observed_at=datetime.now(timezone.utc).isoformat(),
                    verification_evidence=[
                        {"kind": "trust_me", "handle": "unrelated", "observed_result": "claimed"}
                    ],
                )
            )

    def test_effect_observation_cannot_be_future_dated(self):
        with self.assertRaises(ContractError):
            validate_effect_receipt(
                receipt(
                    effect_status="observed_failed",
                    evidence_completeness="complete",
                    acting_surface="filesystem",
                    observed_at="2099-01-01T00:00:00+00:00",
                )
            )

    def test_partial_is_evidence_completeness_not_effect_status(self):
        with self.assertRaises(ContractError):
            validate_effect_receipt(receipt(effect_status="partial"))
        validate_effect_receipt(receipt(evidence_completeness="partial"))

    def test_sensitive_payload_marker_is_rejected(self):
        with self.assertRaises(ContractError):
            validate_effect_receipt(receipt(sensitive_payload_retained=True))

    def test_real_reversible_report_write_produces_valid_success_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.md"
            report.write_text("# Bounded inspection report\n\nNo external action performed.\n")
            digest = hashlib.sha256(report.read_bytes()).hexdigest()
            value = receipt(
                effect_status="observed_succeeded",
                evidence_completeness="complete",
                target=str(report),
                acting_surface="local_filesystem",
                observed_at=datetime.now(timezone.utc).isoformat(),
                verification_evidence=[
                    {
                        "kind": "artifact_sha256",
                        "handle": str(report),
                        "observed_result": digest,
                    }
                ],
            )
            validate_effect_receipt(value)
            self.assertEqual(value["verification_evidence"][0]["observed_result"], digest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
