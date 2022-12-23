import os
from redis import Redis
from fastapi import FastAPI

app = FastAPI()
r = Redis(host=os.environ['DB_HOST'], port=6379, db=0)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{key}")
def read_item(key: str):
    return r.get(key)


@app.post("/items/{key}")
def set_item(key: str, item: str):
    return r.set(key, item)
