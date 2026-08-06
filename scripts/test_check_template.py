#!/usr/bin/env python3
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ["python3", "scripts/check_template.py"]
TARGET = "doctrine/design/decision-records-and-operational-documentation.md"


class SameModelIndependenceCanaryTests(unittest.TestCase):
    def run_with_added_claim(self, claim: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory(prefix="template-canary-") as temp_dir:
            clone = Path(temp_dir) / "repo"
            shutil.copytree(ROOT, clone, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            target = clone / TARGET
            text = target.read_text()
            heading = "## Consequential claim-to-evidence audit (candidate)\n"
            target.write_text(text.replace(heading, f"{heading}\n{claim}\n", 1))
            return subprocess.run(CHECKER, cwd=clone, capture_output=True, text=True)

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


if __name__ == "__main__":
    unittest.main()
