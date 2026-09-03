# code-map.md — File index

Primary file index of this prototype. Read it before exploring the code. Update it whenever a feature, page, table or entry point is added or removed. The folder layout and the rules live in `AGENTS.md` and are not repeated here.

## Features

| Feature | Purpose | Pages | Owner |
|---|---|---|---|
| `example` | Reference slice showing route, service, repository and template. List with a create form. | `/example` | Template |

## Data model

| Table (class) | Purpose | Key fields | Relations |
|---|---|---|---|
| `User` (`app/core/auth.py`) | Sample persons for the fake login | `id`, `email`, `first_name`, `last_name`, `role` | none |
| `OutboundMessage` (`app/core/outbox.py`) | Simulated messages (e-mail, Teams, SAP) | `id`, `channel`, `recipient`, `subject`, `body`, `created_at` | none |
| `ExampleItem` (`app/features/example/models.py`) | Reference entity | `id`, `title`, `description`, `created_at` | none |

## Key entry points

| Path | What it is |
|---|---|
| `app/main.py` | FastAPI app: session middleware, auth guard, routers, `/` and `/lang/{code}` |
| `app/cli.py` | `start`, `seed`, `reset-db`, `check`, `ping` |
| `app/seed.py` | Idempotent synthetic data |
| `app/core/db.py` | Engine, `get_session`, `create_all`, `reset`, model auto-discovery |
| `app/core/auth.py` | Fake login: `User`, `UserRole`, `get_current_user`, sign-in and sign-out routes |
| `app/core/i18n/` | `translate`, `get_language`, `locales/de.json`, `locales/en.json` |
| `app/core/templating.py` | `render(request, template, context)` |
| `app/core/outbox.py` | `send_message` and the `/outbox` page |
| `app/core/excel.py` | `read_rows`, `write_rows` |
| `app/core/logger.py` | JSON logging to stdout |
| `app/templates/base.html` | App shell: header, navigation, language switch, footer |
| `app/templates/components/` | Jinja macros `form_field` and `button` |
| `app/static/app.css` | Project CSS with fallback design tokens |
| `app/design/` | Claude Design bundle (not installed yet) |
| `conftest.py` | Test fixtures `session`, `client`, `signed_in_client` |

## Notable exceptions

*Deviations from the standard feature pattern. Keep in sync with `AGENTS.md` Section 13.*

- *(none yet)*
