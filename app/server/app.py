from fastapi import FastAPI

from .routes.filed import router as FiledRouter

app = FastAPI()

app.include_router(FiledRouter, tags=["Filed"], prefix="/v1/filed")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
