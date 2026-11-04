# Footprint

Footprint is a learning tracker for students. Learners log their learning step by step, which builds a record showing the work was done honestly over time and not at the last minute. They can then share a public portfolio link, with certificates and evidence, on their CV for interviewers.

Final Year Project, BSc (Hons) in Computing (Software Development), National College of Ireland, 2026/27.

## Status

Sprint 0: project set-up. The app has a home page, a small HTMX demo, tests and a CI pipeline. Features such as accounts, learning logs and portfolios come next.

## Tech stack

| Part | Choice | Why |
| --- | --- | --- |
| Back end | Python + Django | Secure defaults (CSRF, password hashing, admin) and quick to build with |
| Front end | Django templates + HTMX | Interactive pages without a separate JavaScript framework |
| Database | PostgreSQL (+ pgvector later) | Reliable relational database; pgvector will store AI embeddings |
| Local dev | Docker Compose | Same set-up on any machine |
| CI | GitHub Actions | Runs the checks below on every push and pull request |
| Code quality | ruff | Linting and formatting |
| Security | bandit, pip-audit (OWASP ZAP later) | Scans our code and our dependencies |

## Running it

### Quick start (SQLite, no Docker)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000

### With Docker and PostgreSQL

```bash
cp .env.example .env
docker compose up --build
```

Open http://localhost:8000

## Checks (the same ones CI runs)

```bash
ruff check .
ruff format --check .
bandit -c pyproject.toml -r .
pip-audit -r requirements.txt
python manage.py test
```

## Project layout

```
config/      Django project settings and main URLs
core/        First app: home page and HTMX demo
templates/   HTML templates
.github/     CI workflow
```
