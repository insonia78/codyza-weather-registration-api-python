from fastapi import FastAPI, status
from routes.accounts import accounts_router
from database.postgres import create_db_and_tables
from supabase import create_client, Client



SUPABASE_URL = "https://lyarynqemuiuesukdkhq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5YXJ5bnFlbXVpdWVzdWtka2hxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5MDk2MzU0MywiZXhwIjoyMTA2NTM5NTQzfQ.1eqk3jTFpbLf8astTITTjsQJGbq7BkD8OlWq0rhyNvY"

supabase_client:Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.include_router(accounts_router)


@app.on_event("startup")
def on_startup():
    # Ensure DB and tables exist before accepting requests
    create_db_and_tables()

@app.get("/health",status_code=status.HTTP_200_OK,tags=["health"])
def read_root():
    return {"Hello": "World"}




