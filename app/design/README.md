# Claude Design bundle

This folder holds the Claude Design export as delivered. Nothing in here is edited by hand;
a new export replaces the folder contents.

- `README.md` (this file) is replaced by the README that ships with the export.
- `project/` holds the export: either a design system (`tokens/`, `components/`, `guidelines/`,
  `ui_kits/`) or finished `*.html` screens with their `assets/`, or both.
- `project/` is served by the app under `/design/`, so token CSS can be linked directly from
  `app/templates/base.html` without copying.

How the agent works with the bundle: `AGENTS.md` Section 8.
