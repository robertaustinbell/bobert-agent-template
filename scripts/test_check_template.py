#!/usr/bin/env python3
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ["python3", "scripts/check_template.py"]
FORMAL_TARGET = "doctrine/design/decision-records-and-operational-documentation.md"


class CanaryHarness(unittest.TestCase):
    def run_copy(self, mutator=None):
        with tempfile.TemporaryDirectory(prefix="template-canary-") as temp_dir:
            clone = Path(temp_dir) / "repo"
            shutil.copytree(ROOT, clone, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            if mutator:
                mutator(clone)
            return subprocess.run(CHECKER, cwd=clone, capture_output=True, text=True)


class ContributorIntakeCanaryTests(CanaryHarness):
    REQUIRED_INTAKE = (
        ".github/ISSUE_TEMPLATE/idea-proposal.yml",
        ".github/ISSUE_TEMPLATE/adoption-runtime-problem.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
    )

    def test_requires_each_contributor_intake_surface(self):
        for relative_path in self.REQUIRED_INTAKE:
            with self.subTest(relative_path=relative_path):
                def mutate(clone, path=relative_path):
                    target = clone / path
                    if target.exists():
                        target.unlink()

                result = self.run_copy(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn(f"missing required file: {relative_path}", result.stdout)

    def test_rejects_loss_of_issue_form_privacy_boundary(self):
        def mutate(clone):
            path = clone / ".github/ISSUE_TEMPLATE/adoption-runtime-problem.yml"
            marker = "I removed credentials, personal records, private prompts or messages"
            path.write_text(path.read_text().replace(marker, "I reviewed the report", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("adoption-runtime-problem.yml", result.stdout)

    def test_rejects_loss_of_agent_submission_authority_boundary(self):
        def mutate(clone):
            path = clone / "CONTRIBUTING.md"
            marker = "An agent must not open an issue, submit a pull request, disclose runtime context, accept a commitment, or communicate externally unless its principal or an authorized workflow permits that action."
            path.write_text(path.read_text().replace(marker, "An agent may submit whenever useful.", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("CONTRIBUTING.md", result.stdout)


class AuthorityEffectContractCanaryTests(CanaryHarness):
    REQUIRED_CONTRACT_FILES = (
        "skills/authority-effect-contracts/SKILL.md",
        "skills/authority-effect-contracts/scripts/contracts.py",
        "skills/authority-effect-contracts/scripts/test_contracts.py",
        "skills/authority-effect-contracts/references/schemas/authority-manifest-v1.schema.json",
        "skills/authority-effect-contracts/references/schemas/external-effect-receipt-v1.schema.json",
    )

    def test_requires_each_contract_surface(self):
        for relative_path in self.REQUIRED_CONTRACT_FILES:
            with self.subTest(relative_path=relative_path):
                def mutate(clone, path=relative_path):
                    target = clone / path
                    if target.exists():
                        target.unlink()

                result = self.run_copy(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn(f"missing required file: {relative_path}", result.stdout)


class ArtifactVerificationCanaryTests(CanaryHarness):
    REQUIRED_FILES = (
        "skills/artifact-verification/SKILL.md",
        "skills/artifact-verification/references/fresh-local-verification.md",
    )
    PROCEDURE_MARKERS = (
        "Capture the narrowest stable source identity available",
        "If the source changes after verification, mark the receipt stale",
    )

    def test_requires_each_artifact_verification_surface(self):
        for relative_path in self.REQUIRED_FILES:
            with self.subTest(relative_path=relative_path):
                def mutate(clone, path=relative_path):
                    target = clone / path
                    if target.exists():
                        target.unlink()

                result = self.run_copy(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn(f"missing required file: {relative_path}", result.stdout)

    def test_rejects_loss_of_source_binding(self):
        def mutate(clone):
            path = clone / "skills/artifact-verification/SKILL.md"
            marker = "If the source changes after verification, mark the receipt stale"
            path.write_text(path.read_text().replace(marker, "Verification remains current after changes", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("artifact-verification/SKILL.md", result.stdout)

    def test_rejects_each_source_binding_clause_relocated_outside_procedure(self):
        for marker in self.PROCEDURE_MARKERS:
            with self.subTest(marker=marker):
                def mutate(clone, phrase=marker):
                    path = clone / "skills/artifact-verification/SKILL.md"
                    text = path.read_text()
                    line = next(line for line in text.splitlines() if phrase in line)
                    text = text.replace(line, "", 1)
                    text += f"\n## Unrelated notes\n\n{line}\n"
                    path.write_text(text)

                result = self.run_copy(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("section 'Procedure' missing required guidance", result.stdout)


class DeterministicEvidenceSourceBindingCanaryTests(CanaryHarness):
    MARKERS = (
        "A producer, executor, or subagent summary is a claim",
        "Bind each verification receipt to the narrowest stable source identity available",
        "Record the evidence-schema version",
        "If any bound source changes, the receipt becomes stale",
        "override actor, authority scope, reason, timestamp, expiry, and affected truth IDs",
        "An override records an authorized acceptance decision; it does not alter the observed verification result or manufacture evidence",
    )

    def test_rejects_each_source_binding_clause_relocated_outside_owner(self):
        for marker in self.MARKERS:
            with self.subTest(marker=marker):
                def mutate(clone, phrase=marker):
                    path = clone / "skills/deterministic-evidence-automation/SKILL.md"
                    text = path.read_text()
                    line = next(line for line in text.splitlines() if phrase in line)
                    text = text.replace(line, "", 1)
                    text += f"\n## Unrelated notes\n\n{line}\n"
                    path.write_text(text)

                result = self.run_copy(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("section 'Outcome-backward verification and source binding' missing required guidance", result.stdout)


class ReadmeGovernedHomesTests(CanaryHarness):
    REQUIRED_HOMES = ("`skills/`", "`decisions/`", "`domain/`", "`evidence/`", "`archive/`", "`log.md`")

    def test_requires_every_governed_home_in_readme(self):
        for home in self.REQUIRED_HOMES:
            with self.subTest(home=home):
                def mutate(clone, marker=home):
                    path = clone / "README.md"
                    path.write_text(path.read_text().replace(marker, "`omitted-home/`", 1))

                result = self.run_copy(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("README.md", result.stdout)


class RuntimeNeutralCalendarAuthorityTests(CanaryHarness):
    def test_rejects_source_specific_calendar_prohibition(self):
        def mutate(clone):
            path = clone / "doctrine/authority/permissions-controls-and-discretion.md"
            marker = "Explicit confirmation; adopter-defined standing policy may prohibit it or authorize a narrower envelope"
            path.write_text(path.read_text().replace(marker, "Prohibited under current standing calendar policy", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Authority matrix", result.stdout)

    def test_rejects_source_specific_customization_default(self):
        def mutate(clone):
            path = clone / "CUSTOMIZE.md"
            marker = "explicit confirmation for calendar mutation and identity-bearing communication unless adopter-defined standing policy is stricter or grants a narrower authorization"
            path.write_text(path.read_text().replace(marker, "default-deny for calendar mutation and identity-bearing communication", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("CUSTOMIZE.md", result.stdout)


class StatisticalEvidenceGateCanaryTests(CanaryHarness):
    def test_rejects_loss_of_search_family_boundary(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "The polished winner is not the evidence"
            path.write_text(path.read_text().replace(marker, "Report the best result", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Statistical-evidence gate", result.stdout)

    def test_rejects_loss_of_imprecise_null_status(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "underpowered or too imprecise"
            path.write_text(path.read_text().replace(marker, "no effect", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Statistical-evidence gate", result.stdout)


class CausalQuestionContractCanaryTests(CanaryHarness):
    def test_rejects_loss_of_identification_boundary(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "Separate the proposed causal model, identification, and estimation"
            path.write_text(path.read_text().replace(marker, "Estimate the association precisely", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Causal-question contract", result.stdout)

    def test_rejects_loss_of_nonidentifiability_status(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "not identifiable from present evidence"
            path.write_text(path.read_text().replace(marker, "estimate anyway", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Causal-question contract", result.stdout)

    def test_rejects_loss_of_individual_attribution_boundary(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "an average population effect does not by itself establish what caused one case"
            path.write_text(path.read_text().replace(marker, "an average effect settles the case", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Causal-question contract", result.stdout)

    def test_rejects_loss_of_identification_regime_boundary(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "specified observational or interventional data regime"
            path.write_text(path.read_text().replace(marker, "available evidence", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Causal-question contract", result.stdout)

    def test_rejects_source_synthesis_hidden_in_comment(self):
        def mutate(clone):
            path = clone / "evidence/sources/book-of-why-pearl-mackenzie-2018.md"
            marker = (
                "Causal diagrams make assumptions inspectable; they do not establish "
                "that those assumptions describe reality."
            )
            path.write_text(path.read_text().replace(marker, f"<!-- {marker} -->", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Agent-design synthesis", result.stdout)


class IdentityAndAdoptionCanaryTests(CanaryHarness):
    def test_rejects_loss_of_installed_candidate_comparison(self):
        def mutate(clone):
            path = clone / "RUNTIMES.md"
            text = path.read_text().replace(
                "compare the installed and candidate versions",
                "assume the candidate supersedes the installed version",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Identity update contract", result.stdout)

    def test_rejects_loss_of_authorized_identity_candidate_source(self):
        def mutate(clone):
            path = clone / "RUNTIMES.md"
            text = path.read_text().replace(
                "resolve the candidate from the adopter-authorized canonical source",
                "accept any candidate carrying a content hash",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Identity update contract", result.stdout)

    def test_rejects_loss_of_reviewed_to_installed_identity_binding(self):
        def mutate(clone):
            path = clone / "RUNTIMES.md"
            text = path.read_text().replace(
                "Activate only the exact acknowledged candidate",
                "Activate the newest available candidate",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Identity update contract", result.stdout)

    def test_rejects_loss_of_identity_update_fallback_probe(self):
        def mutate(clone):
            path = clone / "RUNTIMES.md"
            text = path.read_text().replace(
                "requires an external update process rather than silently activating the candidate",
                "continues with best effort",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Verification probe", result.stdout)

    def test_rejects_loss_of_mechanical_outcome_choice_test(self):
        def mutate(clone):
            path = clone / "SOUL.md"
            text = path.read_text().replace(
                "—meaning no unresolved choice among materially different outcomes remains—",
                "—meaning the work appears routine—",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no unresolved choice among materially different outcomes remains", result.stdout)

    def test_rejects_loss_of_runtime_identity_disclosure_gate(self):
        def mutate(clone):
            path = clone / "ADOPT.md"
            text = path.read_text().replace(
                "Install material-change disclosure as a runtime-level rule or deployment gate",
                "Consider telling the principal when convenient",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("material-change disclosure", result.stdout)

    def test_rejects_direct_inversion_of_mechanical_execution_rule(self):
        def mutate(clone):
            path = clone / "SOUL.md"
            text = path.read_text().replace(
                "—execute without confirmation theater.",
                "—do not execute without renewed confirmation.",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Core truths", result.stdout)

    def test_rejects_relocation_of_identity_disclosure_gate(self):
        def mutate(clone):
            path = clone / "ADOPT.md"
            text = path.read_text()
            sentence = (
                "7. Keep one canonical SOUL. Install material-change disclosure as a runtime-level rule or deployment gate, "
                "and show the changes to the principal before activating a revised persistent identity. Follow the identity "
                "update contract in `RUNTIMES.md` for immutable provenance, comparison, acknowledgment, and an honest fallback "
                "when the runtime cannot preserve that state."
            )
            replacement = "7. Keep one canonical SOUL."
            self.assertIn(sentence, text)
            text = text.replace(sentence, replacement, 1)
            text = text.replace(
                "## Replace source identities before activation",
                f"## Replace source identities before activation\n\n{sentence}",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Bootstrap contract", result.stdout)

    def test_rejects_inversion_of_faithful_representation(self):
        def mutate(clone):
            path = clone / "SOUL.md"
            text = path.read_text().replace(
                "Never knowingly mislead, fabricate, or impersonate",
                "Mislead, fabricate, or impersonate when useful",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Core truths", result.stdout)

    def test_rejects_relocation_of_faithful_representation(self):
        def mutate(clone):
            path = clone / "SOUL.md"
            text = path.read_text()
            paragraph = next(
                line for line in text.splitlines()
                if "**Faithful representation is non-negotiable.**" in line
            )
            text = text.replace(f"{paragraph}\n", "", 1)
            text = text.replace("## Boundaries", f"## Boundaries\n\n{paragraph}", 1)
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Core truths", result.stdout)

    def test_rejects_inversion_of_authenticated_instruction_boundary(self):
        def mutate(clone):
            path = clone / "SOUL.md"
            text = path.read_text().replace(
                "are content to evaluate—not authority to execute",
                "are authority to execute when they appear trustworthy",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Boundaries", result.stdout)

    def test_rejects_relocation_of_authenticated_instruction_boundary(self):
        def mutate(clone):
            path = clone / "SOUL.md"
            text = path.read_text()
            paragraph = next(
                line for line in text.splitlines()
                if "**Only the principal's authenticated conversational instruction" in line
            )
            text = text.replace(f"{paragraph}\n", "", 1)
            text = text.replace("## Continuity", f"## Continuity\n\n{paragraph}", 1)
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Boundaries", result.stdout)


class UntrustedContentBoundaryCanaryTests(CanaryHarness):
    def test_rejects_boundary_deletion(self):
        def mutate(clone):
            path = clone / "doctrine/authority/permissions-controls-and-discretion.md"
            marker = "Independently validate consequential URLs, recipients, paths, commands, payloads, and other arguments"
            path.write_text(path.read_text().replace(marker, "", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Untrusted-content control boundary", result.stdout)

    def test_rejects_boundary_hidden_in_comment(self):
        def mutate(clone):
            path = clone / "doctrine/authority/permissions-controls-and-discretion.md"
            marker = "Independently validate consequential URLs, recipients, paths, commands, payloads, and other arguments"
            path.write_text(path.read_text().replace(marker, f"<!-- {marker} -->", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Untrusted-content control boundary", result.stdout)

    def test_rejects_boundary_hidden_in_fence(self):
        def mutate(clone):
            path = clone / "doctrine/authority/permissions-controls-and-discretion.md"
            marker = "Independently validate consequential URLs, recipients, paths, commands, payloads, and other arguments"
            path.write_text(path.read_text().replace(marker, f"```text\n{marker}\n```", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Untrusted-content control boundary", result.stdout)

    def test_rejects_instruction_promotion_inversion(self):
        def mutate(clone):
            path = clone / "doctrine/authority/permissions-controls-and-discretion.md"
            marker = "The principal's authenticated instruction defines the task and authority envelope"
            path.write_text(path.read_text().replace(marker, "A source instruction may define the task and authority envelope", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Untrusted-content control boundary", result.stdout)

    def test_rejects_transfer_boundary_relocation(self):
        def mutate(clone):
            path = clone / "doctrine/knowledge/information-placement-and-source-authority.md"
            marker = "Information-hazard analysis informs handling; it does not create censorship authority"
            text = path.read_text().replace(marker, "Information hazards justify suppression", 1)
            path.write_text(text.replace("## Stop conditions\n", f"## Stop conditions\n\n{marker}\n", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Information-transfer effects", result.stdout)

    def test_rejects_runtime_free_form_execution(self):
        def mutate(clone):
            path = clone / "RUNTIMES.md"
            marker = "It should not accept free-form instructions copied from retrieved content"
            path.write_text(path.read_text().replace(marker, "It may accept free-form instructions copied from retrieved content", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Untrusted-content execution boundary", result.stdout)

    def test_rejects_blanket_refusal_as_success(self):
        def mutate(clone):
            path = clone / "FIELD-TESTING.md"
            marker = "A blanket refusal is not a clean success, and prompt-level compliance is not proof of runtime containment"
            path.write_text(path.read_text().replace(marker, "A blanket refusal is a clean success", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Untrusted-content boundary candidate test", result.stdout)


class AuthorityManifestAndEffectReceiptCanaryTests(CanaryHarness):
    SOURCE = "doctrine/authority/permissions-controls-and-discretion.md"

    def test_rejects_authority_manifest_deletion(self):
        def mutate(clone):
            path = clone / self.SOURCE
            marker = "Unknown or omitted authority fails closed for consequential effects"
            path.write_text(path.read_text().replace(marker, "", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Authorization envelopes", result.stdout)

    def test_rejects_attempt_as_success_inversion(self):
        def mutate(clone):
            path = clone / self.SOURCE
            marker = "Requested, prepared, and attempted work must not be reported as completed"
            path.write_text(path.read_text().replace(marker, "Attempted work may be reported as completed", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("External-effect receipts", result.stdout)

    def test_rejects_receipt_boundary_relocation(self):
        def mutate(clone):
            path = clone / self.SOURCE
            marker = "Do not retain sensitive payloads merely to make the receipt look complete"
            text = path.read_text().replace(marker, "", 1)
            path.write_text(text.replace("## Stop conditions\n", f"## Stop conditions\n\n{marker}\n", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("External-effect receipts", result.stdout)


class DoctrineTopologyTests(CanaryHarness):
    SOURCE = "doctrine/authority/least-privilege-capability-access.md"

    @staticmethod
    def add_doctrine(clone, *, duplicate_id=False):
        source = clone / DoctrineTopologyTests.SOURCE
        text = source.read_text()
        if not duplicate_id:
            text = text.replace(
                "id: least-privilege-capability-access",
                "id: topology-test-page",
                1,
            ).replace(
                "title: Least-Privilege Capability Access",
                "title: Topology Test Page",
                1,
            )
        target = clone / "doctrine/authority/topology-test-page.md"
        target.write_text(text)
        return target

    def test_accepts_valid_additional_doctrine_page(self):
        def mutate(clone):
            self.add_doctrine(clone)
            generated = subprocess.run(
                ["python3", "scripts/generate_index.py"],
                cwd=clone,
                capture_output=True,
                text=True,
            )
            self.assertEqual(generated.returncode, 0, generated.stdout + generated.stderr)

        result = self.run_copy(mutate)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("9 doctrine pages", result.stdout)

    def test_rejects_duplicate_doctrine_id(self):
        result = self.run_copy(lambda clone: self.add_doctrine(clone, duplicate_id=True))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate doctrine id", result.stdout)

    def test_rejects_malformed_additional_doctrine_page(self):
        def mutate(clone):
            target = clone / "doctrine/authority/topology-test-page.md"
            target.write_text("---\nid: topology-test-page\n---\n\n# Broken\n")

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing type", result.stdout)

    def test_rejects_removal_of_protected_doctrine_page(self):
        def mutate(clone):
            (clone / self.SOURCE).unlink()

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)


class SameModelIndependenceCanaryTests(CanaryHarness):
    def run_with_added_claim(self, claim: str) -> subprocess.CompletedProcess[str]:
        def mutate(clone):
            target = clone / FORMAL_TARGET
            text = target.read_text()
            heading = "## Consequential claim-to-evidence audit (candidate)\n"
            target.write_text(text.replace(heading, f"{heading}\n{claim}\n", 1))

        return self.run_copy(mutate)

    def test_rejects_positive_claim_containing_eg_abbreviation(self):
        result = self.run_with_added_claim(
            "Same-model review, e.g. a second pass, is independent proof."
        )
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("claims same-model review is independent proof", result.stdout)

    def test_accepts_negative_claim_containing_eg_abbreviation(self):
        result = self.run_with_added_claim(
            "Same-model review, e.g. a second pass, is not independent proof."
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_accepts_nothing_about_negative_construction(self):
        result = self.run_with_added_claim(
            "Nothing about a second pass by the same model is independent proof."
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_positive_claims_with_other_nonterminal_periods(self):
        claims = [
            "Same-model review, i.e. another pass, is independent proof.",
            "Same-model review by A. Smith is independent proof.",
            'Same-model review (called "repeat review," e.g. by one agent) is independent proof.',
        ]
        for claim in claims:
            with self.subTest(claim=claim):
                result = self.run_with_added_claim(claim)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("claims same-model review is independent proof", result.stdout)


class SystemsFeedbackCanaryTests(CanaryHarness):
    def test_baseline_passes(self):
        result = self.run_copy()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_timing_canary_rejects_deletion(self):
        def mutate(clone):
            path = clone / "doctrine/design/right-sized-change.md"
            text = path.read_text().replace(
                "Do not launch another corrective cycle merely because the desired result is not yet visible.",
                "Repeated action may occur.",
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("corrective cycle", result.stdout)

    def test_timing_canary_rejects_cross_section_relocation(self):
        def mutate(clone):
            path = clone / "doctrine/design/right-sized-change.md"
            marker = "Do not launch another corrective cycle merely because the desired result is not yet visible."
            text = path.read_text().replace(marker, "Repeated action may occur.", 1)
            path.write_text(text.replace("## Stop conditions\n", f"## Stop conditions\n\n{marker}\n", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Time feedback to the system", result.stdout)

    def test_timing_canary_rejects_same_title_at_wrong_level(self):
        def mutate(clone):
            path = clone / "doctrine/design/right-sized-change.md"
            text = path.read_text().replace("### Time feedback to the system", "#### Time feedback to the system", 1)
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Time feedback to the system", result.stdout)

    def test_operational_friction_rejects_waiting_room_candidate_label(self):
        def mutate(clone):
            path = clone / "doctrine/design/right-sized-change.md"
            text = path.read_text().replace(
                "## Operational-friction check",
                "## Operational-friction check (candidate)",
                1,
            )
            path.write_text(text)

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Operational-friction check", result.stdout)

    def test_boundary_canary_ignores_fenced_marker(self):
        def mutate(clone):
            path = clone / "doctrine/capabilities/external-capability-governance.md"
            marker = "“Out of scope” is an analytical choice, not evidence that excluded effects do not exist"
            text = path.read_text().replace(marker, "A declared boundary defines the complete system")
            path.write_text(text + f"\n```text\n{marker}\n```\n")

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Out of scope", result.stdout)

    def test_boundary_canary_rejects_cross_section_relocation(self):
        def mutate(clone):
            path = clone / "doctrine/capabilities/external-capability-governance.md"
            marker = "“Out of scope” is an analytical choice, not evidence that excluded effects do not exist"
            text = path.read_text().replace(marker, "A declared boundary defines the complete system", 1)
            path.write_text(text.replace("## Stop conditions\n", f"## Stop conditions\n\n{marker}\n", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Boundary and interface fidelity", result.stdout)

    def test_versioned_analysis_canary_rejects_comment_only_marker(self):
        def mutate(clone):
            path = clone / "doctrine/design/decision-records-and-operational-documentation.md"
            marker = "Revalidate the reasoning branches affected by material drift; do not blindly apply stale analysis"
            text = path.read_text().replace(
                marker, "Apply the recorded analysis without checking current state"
            )
            path.write_text(text + f"\n<!-- {marker} -->\n")

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("material drift", result.stdout)


class ValueSensitiveDecisionCanaryTests(CanaryHarness):
    def test_value_boundary_canary_rejects_deletion(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "Preference evidence is not self-interpreting"
            path.write_text(path.read_text().replace(marker, "Preferences settle the comparison", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Preference evidence", result.stdout)

    def test_value_boundary_canary_rejects_cross_section_relocation(self):
        def mutate(clone):
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "A score does not prove commensurability or legitimacy"
            text = path.read_text().replace(marker, "A score settles unlike values", 1)
            path.write_text(text.replace("## Stop conditions\n", f"## Stop conditions\n\n{marker}\n", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Value-sensitive decision boundary", result.stdout)


class RepresentationAdequacyCanaryTests(CanaryHarness):
    def test_representation_boundary_rejects_deletion(self):
        def mutate(clone):
            path = clone / "doctrine/knowledge/information-placement-and-source-authority.md"
            marker = "A representation adequate for one task may be inadequate for another"
            path.write_text(path.read_text().replace(marker, "One compact representation is generally adequate", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Representation adequacy and information loss", result.stdout)

    def test_representation_boundary_rejects_cross_section_relocation(self):
        def mutate(clone):
            path = clone / "doctrine/knowledge/information-placement-and-source-authority.md"
            marker = "Do not fabricate probabilities to enable a metric or describe people as deficient channels"
            text = path.read_text().replace(marker, "Always quantify the representation", 1)
            path.write_text(text.replace("## Stop conditions\n", f"## Stop conditions\n\n{marker}\n", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Representation adequacy and information loss", result.stdout)


class RouterRetrievalTests(unittest.TestCase):
    def test_value_trigger_does_not_displace_model_adequacy_trigger(self):
        result = subprocess.run(
            ["python3", "scripts/generate_index.py", "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        index = (ROOT / "index.md").read_text(encoding="utf-8")
        self.assertIn("contested values", index)
        self.assertIn(
            "the model may omit actors, options, mechanisms, constraints, or feedback",
            index,
        )
        self.assertIn("a consequential representation may omit distinctions that change its downstream task", index)


if __name__ == "__main__":
    unittest.main()
