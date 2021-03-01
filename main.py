from fastapi import FastAPI

from src.routers import similarity

app = FastAPI()
app.include_router(similarity.router)


@app.get("/")
async def root():
    return {"message": "hit this with POST at /text-similarity"}
