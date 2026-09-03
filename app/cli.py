"""Command line entry point: `uv run python -m app.cli <command>`.

start     run the dev server with auto-reload on http://localhost:8000
seed      insert the sample data (idempotent)
reset-db  drop all tables, recreate them and seed
check     format, lint (with fixes) and run all tests
ping      verify that the running app answers
"""

import argparse
import subprocess
import sys

APP_URL = "http://localhost:8000"


def start() -> None:
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


def seed() -> None:
    from app.seed import main

    main()
    print("sample data is in place")


def reset_db() -> None:
    from app.core.db import reset
    from app.seed import main

    reset()
    main()
    print("database reset and seeded")


def check() -> None:
    steps = [
        [sys.executable, "-m", "ruff", "format", "."],
        [sys.executable, "-m", "ruff", "check", "--fix", "."],
        [sys.executable, "-m", "pytest"],
    ]
    for step in steps:
        result = subprocess.run(step, check=False)
        if result.returncode != 0:
            sys.exit(result.returncode)
    print("all checks passed")


def ping() -> None:
    import httpx

    try:
        response = httpx.get(f"{APP_URL}/auth/signin", timeout=3)
    except httpx.HTTPError:
        print("app is NOT running. Start it with: uv run python -m app.cli start")
        sys.exit(1)
    print(f"app answers with status {response.status_code} at {APP_URL}")


COMMANDS = {
    "start": start,
    "seed": seed,
    "reset-db": reset_db,
    "check": check,
    "ping": ping,
}


def main() -> None:
    parser = argparse.ArgumentParser(prog="python -m app.cli", description=__doc__)
    parser.add_argument("command", choices=COMMANDS.keys())
    arguments = parser.parse_args()
    COMMANDS[arguments.command]()


if __name__ == "__main__":
    main()
