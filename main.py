from fastapi import FastAPI
from routers import api


app = FastAPI()
app.include_router(api.router)


@app.get("/")
def home():
    return {"hello": "World!"}
