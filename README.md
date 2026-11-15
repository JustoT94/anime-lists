# Anime Lists Backend

Backend for anime lists project.

## Setup

1. Clone the repo:
   ```bash
   git clone <YOUR_REPO_URL>
   cd anime-lists
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app (development):
   ```bash
   flask run
   ```

## Environment variables

Create a `.env` file in the project root based on `.env.example`:

```bash
cp .env.example .env
```

## Database migrations

To set up and update the database schema:

1. Initialize migrations (only once per project):
   ```bash
   flask db init
   ```

2. Generate a migration after model changes:
   ```bash
   flask db migrate -m "describe your change"
   ```

3. Apply migrations:
   ```bash
   flask db upgrade
   ```