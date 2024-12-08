from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'
    
class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category
    
items = {0 : Item(name = "hammer", price = 9.99, count = 2, id = 0, category=Category.TOOLS),
         1: Item(name = "Saw", price = 10.99, count = 5, id = 1, category=Category.TOOLS)}

fruits = ["Apple", "Orange", "Banana"]
fruitsHash = {0:{"Apple": 0}, 1:{"Banana": 1}, 2:{"Pear": 2}}

@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"item": items}

#Path Params
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item ID doesnt exist")
    return items[item_id]

#Query Params - Use ?
#Example [url/fruits/?fruit_index=0] -> This returns apple
@app.get("/fruits/")
def query_by_params_fruits(fruit_index: int):
    return {"fruit_name": fruits[fruit_index]}

#http://127.0.0.1:8000/fruitsHash/?fruit_id=0&fruit_name=Apple -> For Double query
#Horrible example but needed to show multiple query params
@app.get("/fruitsHash/")
def query_by_params_fruitsHash(fruit_name: str, fruit_id:int):
    return {"fruit_name": fruitsHash[fruit_id], "fruit_id": fruitsHash[fruit_id][fruit_name]}