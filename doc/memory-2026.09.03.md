# Memory 2026.09.03

## Done
- Template scaffolded: FastAPI, Jinja2 and SQLModel on SQLite, fake login, simulated outbox, Excel helper, DE and EN locales, example feature with tests, devcontainer, Claude settings and session-start hook.

## Decisions and assumptions
- One guidance file (`AGENTS.md`), one `doc/code-map.md`, one memory file per day. No further documentation files unless the owner asks for a document.
- The idea, status, result and "needs for the real app" live in `README.md`.
- No migrations: a schema change resets and reseeds the sample database.

## Feedback
- (none)

## Open questions and next steps
- Install the enterprise Claude Design bundle into `app/design/` and link its token CSS in `app/templates/base.html`.
