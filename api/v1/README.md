# Registration API v1

`api/v1` is a FastAPI service for account registration management in the Codyza Weather Project.

## Features

- Health check endpoint
- Create, list, update, partially update, and delete accounts
- PostgreSQL connection through SQLModel and SQLAlchemy
- Database existence check during startup
- Table creation during startup

## Requirements

- Python 3.12 or newer
- PostgreSQL
- `uv`

## Project structure

```text
api/v1/
  controller/
    accounts_controller/
      models/
        models.py
      accounts_controller.py
  database/
    postgres.py
  routes/
    accounts.py
  main.py
  pyproject.toml
```

## Configuration

The service reads its configuration from a local `.env` file.

Required environment variables:

- `POSTGRES_URL`: PostgreSQL connection string used by the application
- `POSTGRES_FILE_NAME`: Database name checked and created at startup if missing

Example shape:

```env
POSTGRES_URL=postgresql+psycopg://username:password@localhost:5432/app_database
POSTGRES_FILE_NAME=app_database
```

## Local development

From the `api/v1` folder:

1. Install dependencies:

   ```powershell
   uv sync
   ```

2. Start the development server:

   ```powershell
   uv run uvicorn main:app --reload
   ```

3. Open the API docs:

   - `http://127.0.0.1:8000/docs`
   - `http://127.0.0.1:8000/redoc`

## Startup behavior

When the application starts:

1. It loads values from `.env`
2. It connects to PostgreSQL
3. It checks whether the configured database exists
4. It creates the database if needed
5. It creates the SQLModel tables

## Endpoints

### Health

#### `GET /health`

Returns:

```json
{
  "Hello": "World"
}
```

### Accounts

#### `GET /accounts/`

Returns all accounts.

#### `POST /accounts/`

Creates an account.

Example request body:

```json
{
  "email": "user@example.com",
  "password": 1234
}
```

#### `PUT /accounts/{id}`

Replaces an existing account.

Example request body:

```json
{
  "email": "updated@example.com",
  "password": 5678
}
```

#### `PATCH /accounts/{id}`

Partially updates an existing account.

Example request body:

```json
{
  "email": "patched@example.com"
}
```

#### `DELETE /accounts/{id}`

Deletes an account and returns the deleted record.

## Data model

The current account model includes:

- `id: int`
- `email: str`
- `password: int`

## Notes

- The current implementation returns `404` when an account is not found for update, patch, or delete operations.
- Database errors are surfaced as `500` responses.
- The API currently creates tables automatically on startup.
