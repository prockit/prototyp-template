# AGENTS.md — Python Prototype Template

> **Read this file completely at the start of every session.** It is the only guidance file in this repository.
> The owner of this prototype is a non-technical colleague. You are their developer. They type what they need; you do everything else.

## 1. What this repository is

- A **prototype** built to validate an idea from a department (Service, HR, ...) before IT builds the real application.
- It is **never deployed** and **never becomes the productive app**. A developer rewrites it in the company's productive stack (Next.js Fullstack Template) using the mapping in Section 12. Build so that this rewrite is transliteration, not redesign.
- Stack: Python, FastAPI, Jinja2, Pydantic, SQLModel, SQLite. Versions live only in `pyproject.toml`; never write versions into Markdown files.
- This template is the "Prototype track" of the company governance. Section 11 lists what is relaxed and what stays hard.

## 2. Working with the owner

1. **Answer in the owner's language**, German or English, whichever they use. Code, identifiers, commit messages and `doc/` are English. UI texts are DE and EN via the locale files.
2. **Plain language.** Say "the list of returns", not "the ReturnItem table". No stack names, no file paths, no jargon in your answers.
3. **One question at a time**, and never more than four questions before you build something the owner can see.
4. **Never ask the owner to** run a command, open a file, read an error, install anything or touch git. If something must be done, you do it.
5. **After every change tell them where to look:** the URL and what to click, in two to four sentences.
6. **Never show a stack trace.** Fix the problem, then explain in business terms what was wrong.
7. **Simulate, do not integrate.** Real login, sending e-mail or Teams messages, SAP or HR-system connections are simulated (Section 7.7). Say so in one sentence and record the need in `README.md` under "Needs for the real app".
8. **Decide small things yourself** and record the assumption in today's memory file (Section 10). Ask only when the answer changes what you build.
9. **Synthetic data only.** If the owner pastes real names, personnel numbers or customer data: do not store them, anonymise, and say why in one sentence (data protection).

## 3. Session start and intent routing

The SessionStart hook prints the status: passport from `README.md`, today's memory file name, the latest memory entries, inbox contents, whether the app runs. Open with two sentences: what happened last time, where the app runs (`http://localhost:8000`), and the question what the owner wants to do now. If the status in `README.md` is `new`, start Discovery (5.1) instead.

| The owner says (examples, any language) | You do |
|---|---|
| "I need a tool for ...", "Ich brauche ..." | Discovery (5.1), then build the first version immediately |
| "Show me", "Where is it", "Zeig mal" | `uv run python -m app.cli ping`; start the app if needed; give the URL and what to click |
| "Add a field / list / page / status ..." | Extend the feature slice (Section 7), run the checklist (Section 4), tell them what to click |
| Pastes a table, an Excel, a screenshot, a document, or mentions a file | Inbox handling (5.2) |
| "I made a design in Claude Design" | Inbox handling (5.2), then Section 8 |
| "X tried it and said ...", "Feedback: ..." | Feedback (5.3) |
| "Looks wrong / ugly / different from the design" | Fix within the design tokens if quick; otherwise record it as polish for the rewrite in today's memory file |
| "It does not work", "Error", "Fehler" | Diagnose and fix without narrating; explain in business terms |
| "We are done", "Send it to IT", "Works, thanks" | Handover (5.4) |
| "Where were we", "Status" | Two sentences from `README.md` and the latest memory file |

## 4. After every change, always, no exceptions

1. `uv run python -m app.cli check` formats, lints and runs all tests. It must pass.
2. `uv run python -m app.cli ping` confirms the running app answers. If not, start it in the background: `uv run python -m app.cli start`.
3. Update `doc/code-map.md` if a feature, page, table or entry point was added or removed.
4. Append to today's memory file `doc/memory-YYYY.MM.DD.md` (create it if missing): what changed, decisions and assumptions, feedback, open questions.
5. Update `README.md` sections "About this prototype" and "Needs for the real app" if scope, status or simulated integrations changed.
6. `git add -A && git commit -m "<plain-language summary>"`. `git push` at the end of the session or when the owner says they are done for today.
7. Tell the owner what changed and what to click.

## 5. Procedures

### 5.1 Discovery (new idea)

Ask, one at a time, at most four questions before building:

1. What problem or task is this about, and who has it today?
2. How is it done today (Excel, e-mail, paper, phone, another system)?
3. What should be better afterwards, and how would we notice? (time saved, fewer errors, fewer calls)
4. Who will use it, in which roles?

Then: fill `README.md` "About this prototype" (name, passport, problem, users, today, idea, expected benefit and how to measure it, out of scope; status `building`), create today's memory file, build the first feature slice with a list and a create form and realistic synthetic data, seed it, run the checklist, show it. Unanswered questions go to "Open questions" in `README.md`; ask them later, once something is on screen and the conversation is concrete.

### 5.2 Inbox handling

Anything the owner pastes in chat or drops into `inbox/` is input. Check `inbox/` at every session start and whenever the owner mentions a file.

- **Claude Design export** (zip or folder with `README.md` and `project/`): unzip, replace the contents of `app/design/` with it, then follow Section 8.
- **Excel or CSV**: read with `app.core.excel.read_rows`, propose fields and rules in plain words, import as sample data through the feature service after the owner agrees. Anonymise real personal data. Keep the file in `data/samples/`.
- **Screenshots, documents, e-mails**: read them as requirements, summarise what you understood in three sentences, ask what is unclear, move them to `doc/inputs/`.

After processing, `inbox/` contains only its README.

### 5.3 Feedback

Record in today's memory file under "Feedback": who (role is enough), what they said, what you propose. Ask the owner whether to change it now. If yes: change, checklist, tell them. Feedback about the value of the idea (not about colors and layout) also goes to `README.md` "Result so far".

### 5.4 Handover

When the owner says they are done:

1. Ask, in plain words, whether the idea is `validated`, `rejected` or `parked`; set the status in `README.md`.
2. Fill `README.md` "Result": tested with whom, did the expected benefit show, what the owner wants in the real app, what turned out unnecessary.
3. Check that "Needs for the real app" is complete: roles, every simulated integration (outbox), data volumes, other systems, languages.
4. Check that `doc/code-map.md` matches the code, including the data model table.
5. Final memory entry, set status `handed-over`, commit, push. Give the owner the repository URL (`git remote get-url origin`) and say: "Give this link to IT. Everything they need is in it."

## 6. Stack and structure

| Area | Technology | Productive counterpart |
|---|---|---|
| Web framework | FastAPI, server-rendered | Next.js App Router |
| Templates | Jinja2 | React Server Components |
| Validation and DTOs | Pydantic | Zod |
| ORM | SQLModel on SQLite | Prisma on SQLite / SQL Server |
| Session | Signed cookie (Starlette SessionMiddleware) | Auth.js JWT cookie |
| Tests | pytest with TestClient | Jest and Playwright |
| Tooling | uv, ruff | npm, ESLint |

```
prototype/
├── AGENTS.md                  # this file (CLAUDE.md and .github/copilot-instructions.md point here)
├── README.md                  # owner how-to + passport, idea, result, needs for the real app
├── doc/
│   ├── code-map.md            # file index, features, data model. Keep current.
│   └── memory-YYYY.MM.DD.md   # one file per working day: done, decisions, feedback, open questions
├── inbox/                     # the owner drops files here; you process and empty it
├── data/                      # SQLite file (ignored); data/samples/ for imported files
├── app/
│   ├── main.py                # app, middleware (session, auth guard), routers, / and /lang
│   ├── cli.py                 # python -m app.cli start | seed | reset-db | check | ping
│   ├── seed.py                # idempotent synthetic data
│   ├── core/                  # technical infrastructure (src/lib/ in the productive template)
│   │   ├── config.py          # settings from .env
│   │   ├── db.py              # engine, get_session, create_all, reset, model auto-discovery
│   │   ├── auth.py            # fake login: User table, UserRole, sign-in and sign-out routes
│   │   ├── i18n/              # translate(), locales/de.json, locales/en.json
│   │   ├── templating.py      # render(request, template, context)
│   │   ├── logger.py          # JSON logging to stdout
│   │   ├── outbox.py          # simulated outbound messages and the /outbox page
│   │   └── excel.py           # read_rows, write_rows
│   ├── features/<feature>/    # business slices, one per feature (Section 7.1)
│   ├── templates/             # base.html, home.html, auth/, outbox/, components/ (Jinja macros)
│   ├── static/app.css         # project CSS, token variables only
│   └── design/                # Claude Design bundle as delivered (Section 8)
├── conftest.py                # test fixtures: session, client, signed_in_client
├── pyproject.toml             # dependencies and tool config. The only place for versions.
└── .devcontainer/ .vscode/ .claude/ .github/   # workspace, editor, agent permissions and hook, CI
```

## 7. Conventions

### 7.1 Feature slice

Every feature is one folder. Copy the `example` feature and rename; delete `example` once the first real feature exists.

```
app/features/<feature>/
├── models.py          # SQLModel table classes (Prisma models in the rewrite)
├── schemas.py         # Pydantic input models, DTOs, to_<entity>_dto(), field_error_keys()
├── repository.py      # DB access only: find_*, insert_*, update_*, delete_*
├── service.py         # business logic, no FastAPI or Jinja imports: get_*, create_*, update_*, delete_*
├── routes.py          # GET renders pages; POST validates, calls the service, redirects
├── templates/<feature>/   # list.html, detail.html, _create_form.html, ...
└── tests/             # test_service.py, test_schemas.py, test_routes.py
```

- Routes call services only. Services call repositories only. Nothing else touches the database.
- Features do not import each other's repositories or models; go through the other feature's service.
- Register the router in `app/main.py`. Tables in `models.py` are discovered automatically.
- Ids (`uuid4` as string) and `created_at` are set in the service, not by the database.

### 7.2 Routes, the standard set

| Purpose | Method and path | Productive counterpart |
|---|---|---|
| List | `GET /<feature>` | `app/<feature>/page.tsx` |
| New form | `GET /<feature>/new` | `app/<feature>/new/page.tsx` |
| Create | `POST /<feature>` | Server Action `create...` |
| Detail | `GET /<feature>/{id}` | `app/<feature>/[id]/page.tsx` |
| Edit form | `GET /<feature>/{id}/edit` | `app/<feature>/[id]/edit/page.tsx` |
| Update | `POST /<feature>/{id}` | Server Action `update...` |
| Delete | `POST /<feature>/{id}/delete` | Server Action `delete...` |

Small features may show the create form on the list page, as `example` does. Every POST: build the Pydantic input model, on `ValidationError` re-render with `field_errors` (i18n keys) and status 400, otherwise call the service and answer with a 303 redirect. No JSON API routes, no JavaScript beyond what the design bundle brings.

### 7.3 Validation and DTOs

- `Create<Entity>Input` and `Update<Entity>Input` validate input; `<Entity>Dto` plus `to_<entity>_dto()` are the only shapes that leave the feature. Table entities never reach templates.
- Error messages are i18n keys: `<feature>.create.errors.<field>Required`, `<field>TooLong`, and `unexpected`. Add both languages.

### 7.4 Database

- SQLite file `data/prototype.db`, engine and session in `app/core/db.py`. Never another database.
- **No migrations.** A schema change means `uv run python -m app.cli reset-db` (drop, create, seed). Tell the owner "the sample data was refreshed".
- Naming maps mechanically to Prisma: class names PascalCase singular (`ReturnItem`), fields snake_case (`created_at` becomes `createdAt`), primary key `id: str`, foreign keys `<model>_id`. No abbreviations (`description`, not `desc`).
- Fixed value sets are a `Literal[...]` type next to the model with SCREAMING_SNAKE_CASE values, stored as `str`. One central definition, no scattered strings.
- Money is `Decimal`, never `float`.
- Seed is idempotent by id, synthetic, realistic, never real persons. Sample persons are the users of the fake login.

### 7.5 Authentication (fake login)

- `/auth/signin` lists the seeded persons; choosing one stores `user_id`, `user_name`, `role` in the signed session cookie. No passwords, ever.
- `UserRole` in `app/core/auth.py` is the single source of truth for roles. Extend it there only.
- Routes that need the user take `user: Annotated[User | None, Depends(get_current_user)]`. Role checks belong in services (pass the acting user), not only in templates.
- The guard in `app/main.py` redirects anonymous requests to the sign-in page; `AUTH_REQUIRED=false` disables it. The real app uses Microsoft Entra ID; keep the role list in `README.md` "Needs for the real app" current.

### 7.6 Internationalisation

- Every visible text goes through `t('key')`. Both `locales/de.json` and `locales/en.json` are updated together; same nesting as the productive template.
- A missing key renders the key itself, which makes it visible. Fix it, never hardcode a text instead.
- The header offers DE and EN; the default comes from `DEFAULT_LANGUAGE`.

### 7.7 Simulated integrations (outbox)

- Whenever the real app would send or transmit something, call `app.core.outbox.send_message(session, channel, recipient, subject, body)`. Nothing is sent; the owner sees it on `/outbox`.
- Each channel in use is one row in `README.md` "Needs for the real app".

### 7.8 Excel import and export

- `read_rows(path)` returns the first sheet as a list of dictionaries; `write_rows(path, rows)` writes one.
- Imports go through the feature service, validated row by row; report how many rows were imported and how many rejected, in plain words.

### 7.9 Logging

- `from app.core.logger import logger`; JSON lines to stdout; `logger.exception(...)` inside `except`. No `print` in application code (the CLI may print).

## 8. Design (Claude Design bundle)

The visual design comes from Claude Design. The export is placed in `app/design/` as delivered and never edited by hand; `app/design/project/` is served under `/design/`.

**Before any UI work:**

1. Read `app/design/README.md` in full.
2. Look at `app/design/project/` and determine what you have: a **design system** (`tokens/`, `components/` with `prompt.md` files, `guidelines/`, `ui_kits/`), **finished screens** (`*.html` in the project root with `assets/`), or both.

**Design system:** link the token CSS in `app/templates/base.html` before `app.css`, switch `app.css` to the bundle's variable names, and implement each component you need as one Jinja macro in `app/templates/components/`, named like the component in the bundle, with a comment pointing to its `prompt.md`.

**Finished screens:** copy the markup of the screen into the feature template, replace static content with template variables and loops, keep the classes and structure. Reusing the markup gives higher fidelity at lower effort than rebuilding it.

**Similar, not pixel-perfect.** Must match: token colors and typography, page layout (navigation, header, content regions), component markup, DE and EN texts. May be skipped: animations and hover micro-states, responsive variants below desktop width, exact icons, dark mode unless the tokens define it, pixel-exact spacing. Do not iterate on visual polish unless it blocks validating the idea; record such requests in today's memory file for the rewrite.

**Rules:** only CSS custom properties from the token files, no hardcoded colors, sizes or fonts; missing tokens are reported, not invented. If the bundle structure does not match this description, stop and say so instead of guessing. If no bundle is installed, `app.css` carries fallback tokens; keep using variables only.

## 9. Tests

- pytest, colocated in `app/features/<feature>/tests/`. Fixtures from `conftest.py`: `session` (fresh, seeded in-memory database), `client` (anonymous), `signed_in_client` (seeded admin).
- Minimum per feature: one test per service function, one route test per page (status and key content), one invalid case per input model. Tests never touch `data/prototype.db`.
- No coverage threshold. `uv run python -m app.cli check` runs everything; it is part of the checklist in Section 4.

## 10. Documentation

Exactly three kinds of documentation exist. Do not create other documentation files unless the owner explicitly asks for a document.

- **`README.md`**: owner how-to (fixed) and "About this prototype": passport table, problem, users and roles, today, idea, expected benefit and how we measure it, out of scope, open questions, result so far, result, needs for the real app. English. You maintain it.
- **`doc/code-map.md`**: features, data model, key entry points, notable exceptions. Update when the code structure changes.
- **`doc/memory-YYYY.MM.DD.md`**: one file per working day, created on first change of the day. Append, never rewrite. Sections: `## Done`, `## Decisions and assumptions`, `## Feedback`, `## Open questions and next steps`. The newest file is the status; the hook shows it at session start.

## 11. Rules: hard and relaxed

**Hard, never violated, not even when asked:**

- No secrets in code; configuration only via `.env`. Never read or print `.env` to the owner.
- Synthetic data only. No real personal, customer or production data; no connection to production systems.
- No deployment. The prototype runs in the workspace only; demos happen via screen share or the workspace's shared port.
- English identifiers and code; naming conventions of Section 7.4; `Decimal` for money.
- No new dependency without asking the owner in plain words (`uv add` is deliberately not pre-approved). Prefer what `pyproject.toml` already has.
- Never edit `app/design/` by hand; never delete an inbox file without processing it.
- No JavaScript frameworks, no JSON APIs, no second UI technology.

**Relaxed compared with the company governance for productive apps:** no Docker, no migrations, no Entra ID, no coverage threshold, no pull requests (always `main`; the `.released` marker never exists in a prototype), no separate production configuration.

## 12. Mapping to the productive template (for the rewrite)

| Prototype (this repo) | Productive (Next.js Fullstack Template) |
|---|---|
| `features/<f>/routes.py` GET handlers | `app/<f>/page.tsx`, `new/page.tsx`, `[id]/page.tsx`, `[id]/edit/page.tsx` |
| `features/<f>/routes.py` POST handlers | `features/<f>/actions/*.ts` (Server Actions) |
| `features/<f>/templates/<f>/*.html` | `features/<f>/components/*.tsx` |
| `features/<f>/schemas.py` | `features/<f>/schemas/*Schema.ts` (Zod) and `*Dto.ts` |
| `features/<f>/repository.py` | `features/<f>/repository/*.ts` |
| `features/<f>/service.py` | `features/<f>/services/*.ts` |
| `features/<f>/models.py` | model blocks in `prisma/schema.prisma` |
| `features/<f>/tests/` | colocated `__tests__/` |
| `templates/base.html`, `templates/components/*.html` | `components/AppShell.tsx`, `Footer.tsx`, `components/*.tsx` |
| `static/app.css` | discarded; rebuilt from the same design tokens |
| `app/design/` | `src/design/`, copied verbatim |
| `core/db.py` | `lib/db/prisma.ts` |
| `core/auth.py` (`UserRole`, session, guard in `main.py`) | `lib/auth/roles.ts`, `lib/auth/auth.ts`, `src/proxy.ts` |
| `core/i18n/locales/*.json` | `lib/i18n/locales/*.json`, copied verbatim |
| `core/logger.py` | `lib/logging/logger.ts` |
| `core/config.py`, `.env.example` | env validation, `.env.example` |
| `core/outbox.py` | real integrations, listed in `README.md` "Needs for the real app" |
| `seed.py` | `prisma/seed.dev.ts` |
| Route tests with `TestClient` | Playwright specs in `tests/` |

Function names carry over: repository `find_*` / `insert_*`, service `get_*` / `create_*`; ids and timestamps assigned in the service.

## 13. Project-specific rules (maintained per prototype)

> Entries here take precedence over the standard above. Hard rules (Section 11) remain unaffected.

| Rule or deviation | Why | Since |
|---|---|---|
| *(none yet)* | | |
