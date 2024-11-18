from fastapi import FastAPI
from app.routes import router
from app.database import init_db

app = FastAPI()


@app.on_event("startup")
async def startup_db():
    await init_db()


app.include_router(router)
