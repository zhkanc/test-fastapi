from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


items: dict[int, Item] = {}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def list_items():
    return list(items.values())


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        return {"error": "Item not found"}
    return item


@app.post("/items")
async def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, "item": item}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return {"id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item = items.pop(item_id, None)
    if not item:
        return {"error": "Item not found"}
    return {"deleted": item_id}
