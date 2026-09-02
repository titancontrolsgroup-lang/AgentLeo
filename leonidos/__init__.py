"""Leonidos — small helpers for Patrick Olson's Microsoft 365 assistant.

This package is a starter, not a full application. Policy constants live here so
Cursor agents have real code to extend without inventing an unrelated app.
"""

from leonidos.policy import (
    NEVER_SEND_EMAIL,
    OUTLOOK_MODE,
    PHI_IN_REPO,
    assert_safe_to_commit,
)

__all__ = [
    "NEVER_SEND_EMAIL",
    "OUTLOOK_MODE",
    "PHI_IN_REPO",
    "assert_safe_to_commit",
]
