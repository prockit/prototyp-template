#!/usr/bin/env bash
# SessionStart hook: prints the prototype status into the agent's context so the
# agent can greet the owner with "last time we ..., the app runs here, what next?".
cd "$(dirname "$0")/../.." || exit 0

echo "=== Prototype status ==="
grep -E '^\| \*\*(Name|Department|Owner|Status)\*\*' README.md 2>/dev/null || echo "README passport not filled yet"

today="$(date +%Y.%m.%d)"
echo "today: $today  -> memory file: doc/memory-$today.md"

latest="$(ls doc/memory-*.md 2>/dev/null | sort | tail -n 1)"
if [ -n "$latest" ]; then
  echo "--- latest memory file: $latest (last 30 lines) ---"
  tail -n 30 "$latest"
else
  echo "no memory file yet"
fi

inbox_files="$(ls -A inbox 2>/dev/null | grep -v '^README.md$')"
if [ -n "$inbox_files" ]; then
  echo "--- inbox contains new files, process them (AGENTS.md 5.2) ---"
  echo "$inbox_files"
else
  echo "inbox: empty"
fi

if curl -s -o /dev/null -m 2 http://localhost:8000/auth/signin; then
  echo "app: running at http://localhost:8000"
else
  echo "app: NOT running. Start it in the background: uv run python -m app.cli start"
fi
