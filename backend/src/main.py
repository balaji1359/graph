from typing import Union
from db.queries.basic import get_basic
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://18.221.40.209:3000",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://45.55.42.215:8000",
    "http://127.0.0.1:8000/",
    "http://45.55.42.215:3000"
    "45.55.42.215:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return get_basic()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
