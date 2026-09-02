# AgentLeo (Leonidos)

Cursor working repository for **Leonidos**, Patrick Olson’s Microsoft 365 assistant.

This repo exists so Patrick can keep working with Cursor (desktop and cloud agents). Cursor needs a GitHub repository to attach to; this is that repo.

## Who and what

Leonidos helps Patrick with day-to-day Microsoft 365 work around **Crothall / MedStar** hospital sites:

| Area | What Leonidos does |
| --- | --- |
| **Outlook** | Prepare messages as **drafts only**. Never send mail. |
| **Calendar** | Read and help manage the schedule. |
| **OneDrive** | Find, organize, and draft file work. |
| **OneNote** | Structure hospital / site notes (operational, not patient records). |

Leonidos is an assistant, not a product app. Work happens in Microsoft 365; this repository holds context, rules, and templates so Cursor agents can pick up where Patrick left off.

## How to use this repo with Cursor

1. Open [titancontrolsgroup-lang/AgentLeo](https://github.com/titancontrolsgroup-lang/AgentLeo) in Cursor (File → Open Folder, or start a Cloud Agent on this repo).
2. Ask in plain language, for example:
   - “Draft a reply to this email, don’t send it.”
   - “What’s on my calendar tomorrow?”
   - “Find the latest file in OneDrive about [topic].”
   - “Turn these site notes into a OneNote hospital-note outline.”
3. Review Outlook drafts in Outlook itself before you send anything.
4. Keep secrets out of git. Put tokens in Cursor / MCP auth, never in files here.

Cloud agents need a non-empty repo with real files. The starter layout below is enough to attach and iterate.

## Hard rules

- **Never send email.** Outlook work is drafts-only.
- **Do not commit secrets**, tokens, passwords, or `.env` files.
- **Do not store patient health information (PHI)** in this repository.
- Prefer small, professional changes over a large unrelated app.

These rules are also in `AGENTS.md` and `.cursor/rules/leonidos.mdc`.

## Layout

```
.
├── README.md                 # This file
├── AGENTS.md                 # How Cursor agents should work here
├── .gitignore
├── .cursor/rules/leonidos.mdc
├── docs/scope.md             # What is in / out of scope
├── templates/                # Draft and hospital-note outlines
└── leonidos/                 # Tiny policy helpers (not a full app)
```

## Owner

Patrick Olson (`patrickolson@outlook.com`), GitHub org [titancontrolsgroup-lang](https://github.com/titancontrolsgroup-lang).
