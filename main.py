from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Home Page"}

@app.get("/about")
def about():
    return{"message": "About Page"}

inventory = {
    1: {
        "name": "Apple",
        "price": 3.99,
        "quantity": 5
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="ID of item")): #Code is saying if there is no passed value, default is None
    return {"Item" : inventory[item_id]}