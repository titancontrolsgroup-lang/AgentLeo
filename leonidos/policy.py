"""Hard operating rules for Leonidos.

These values are the source of truth for agent behavior in this repo.
Do not weaken them.
"""

from __future__ import annotations

NEVER_SEND_EMAIL = True
OUTLOOK_MODE = "drafts_only"
PHI_IN_REPO = False

_SECRET_MARKERS = (
    "api_key",
    "secret",
    "password",
    "token",
    "bearer ",
    "private_key",
)


def assert_safe_to_commit(text: str) -> None:
    """Raise ValueError if *text* looks like a secret or PHI dump.

    This is a coarse guard for local checks, not a compliance scanner.
    """
    lowered = text.lower()
    for marker in _SECRET_MARKERS:
        if marker in lowered:
            raise ValueError(
                "Refusing to treat this text as repo-safe: looks like a secret. "
                "Keep tokens in Cursor / MCP auth, never in git."
            )
