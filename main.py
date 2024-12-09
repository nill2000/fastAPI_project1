from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]
    
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

@app.get("/")
def root():
    return{"message": "Home Page"}

@app.get("/about")
def about():
    return{"message": "About Page"}

inventory = {}

#Path Params
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., title="ID of item", gt=0)): #Code is saying if there is no passed value, default is None
    return {"Item" : inventory[item_id]}

#Query Params -> http://127.0.0.1:8000/get-by-name/?item_name=Apple
@app.get("/get-by-name/")
def get_item(item_name: str = None): #Code is saying if there is no passed value, default is None
    for item_id in inventory:
        if inventory[item_id].name == item_name:
            return inventory[item_id]
        else:
            return {"msg": "Not Found"}
        
# #Both Path and Query Params
# @app.get("/get-by-name/{item_id}")
# def get_item(item_name: str = None): #Code is saying if there is no passed value, default is None
#     for item_id in inventory:
#         if inventory[item_id]["name"] == item_name:
#             return inventory[item_id]
#         else:
#             return {"msg": "Not Found"}
        
#Use the docs to post and use the get request to test out the database
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
	if item_id in inventory:
		return "Error: Already Exists"
	inventory[item_id] = item
	return inventory[item_id]

#Updates an existing item
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item:UpdateItem):
    if item_id not in inventory: #If item doesn't exist, can't update
        return {"error": "Item does not exist"}
    
    #If so, change the item at said id with new contents
    #By default, values are None from the UpdateItem class, if it isn't None, update the contents
    #None is needed because what if you dont want to  update contents
    if item.name != None:
        inventory[item_id].name = item.name 
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id] #Return the new item for output
 
#Deletes item with associated id
@app.delete("/delete-item/")
def delete_item(item_id: int = Query(..., description="Id of item to delete")):
    if item_id not in inventory:
        return {"Error": "Item ID dont exist"}
    del inventory[item_id]
    return {"msg": "Item has been deleted"}
    
     
    


     
	


	