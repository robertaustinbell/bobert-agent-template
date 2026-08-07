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
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
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
            path = clone / "doctrine/decisions/decision-quality-under-uncertainty.md"
            marker = "Do not launch another corrective cycle merely because the desired result is not yet visible."
            text = path.read_text().replace(marker, "Repeated action may occur.", 1)
            path.write_text(text.replace("## Stop conditions\n", f"## Stop conditions\n\n{marker}\n", 1))

        result = self.run_copy(mutate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Time feedback to the system", result.stdout)

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


if __name__ == "__main__":
    unittest.main()
