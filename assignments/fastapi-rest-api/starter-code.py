from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ItemInput(BaseModel):
    name: str
    description: str


class Item(ItemInput):
    id: int


items: dict[int, Item] = {}
next_item_id = 1


@app.get("/items", response_model=list[Item])
def list_items():
    # Return all items.
    pass


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    # Return the requested item or raise HTTPException with status code 404.
    pass


@app.post("/items", response_model=Item, status_code=201)
def create_item(item_input: ItemInput):
    # Create an item with a unique ID and add it to items.
    pass


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_input: ItemInput):
    # Replace the requested item, or raise HTTPException if it does not exist.
    pass


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    # Delete the requested item, or raise HTTPException if it does not exist.
    pass


# Run with: uvicorn starter-code:app --reload