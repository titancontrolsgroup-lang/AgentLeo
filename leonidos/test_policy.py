"""Tests for Leonidos safety policy."""

from __future__ import annotations

import unittest

from leonidos.policy import (
    NEVER_SEND_EMAIL,
    OUTLOOK_MODE,
    PHI_IN_REPO,
    assert_safe_to_commit,
)


class PolicyTests(unittest.TestCase):
    def test_email_is_drafts_only(self) -> None:
        self.assertTrue(NEVER_SEND_EMAIL)
        self.assertEqual(OUTLOOK_MODE, "drafts_only")

    def test_phi_stays_out_of_repo(self) -> None:
        self.assertFalse(PHI_IN_REPO)

    def test_safe_prose_is_allowed(self) -> None:
        assert_safe_to_commit("Draft a follow-up about the loading dock schedule.")

    def test_secret_like_text_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            assert_safe_to_commit("password=hunter2")


if __name__ == "__main__":
    unittest.main()
