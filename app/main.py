from typing import Optional
from fastapi import FastAPI

import majan_point

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/result/kokushi")
def get_kokushi_point():
    mp = majan_point.MajanPoint()
    return { "point": mp.calc_kokushi() }
