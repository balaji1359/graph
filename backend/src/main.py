from typing import Union
from db.queries.basic import get_basic
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return get_basic()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}