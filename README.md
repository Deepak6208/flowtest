# flowtest

Demonstration repository for the team Git workflow: branching, pull requests,
code review, automated checks, and promotion through dev, staging and production.

The application itself is deliberately trivial. It exists so the process around
it can be shown end to end.

## Endpoints

- `GET /health` — liveness check
- `GET /config` — service name and supported insurance lines

## Running locally

    docker compose up --build

Then open http://localhost:8000/config

## Tests

    pytest -v

## Workflow

See the Git Workflow Policy document. In short: no direct commits to `main`,
every change arrives via pull request, one approval plus passing checks are
required to merge, and merges are squashed.
