from typing import Optional
from fastapi import FastAPI

from routers import point
from routers import wait

app = FastAPI()
app.include_router(point.router)
app.include_router(wait.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

