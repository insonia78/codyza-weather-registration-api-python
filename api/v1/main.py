from fastapi import FastAPI, status
from routes.accounts import accounts_router
from database.postgres import create_db_and_tables
# from supabase import create_client, Client


app = FastAPI()

app.include_router(accounts_router)


@app.on_event("startup")
def on_startup():
    # Ensure DB and tables exist before accepting requests
    create_db_and_tables()

@app.get("/health",status_code=status.HTTP_200_OK,tags=["health"])
def read_root():
    return {"Hello": "World"}




