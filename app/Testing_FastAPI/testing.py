# # User - Nilesh
# # Dependency Installation: pip install fastapi | pip install uvicorn


# from fastapi import FastAPI, HTTPException


# app = FastAPI()

# items = []

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# # To start the server, run the following command in your terminal:
# # uvicorn user:app --reload
# # In here user is the name of the file without the .py extension 
# # while app is the FastAPI instance.

# @app.post("/items")
# def create_item(item: str):
#     items.append(item)
#     return items

# # To test the POST endpoint, you can use curl.
# # curl -X POST -H "Content-Type: application/json" 'http://127.0.1:8000/items?item=apple'


# @app.get("/items")
# def list_items(limit: int = 10):
#     return items[:limit]
# # This set the default limit to 10 items.
# # curl -X GET 'http://127.0.1:8000/items?limit=5'

# @app.get("/items/{item_id}")
# def get_item(item_id: int) -> str:
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")

# # To get item by ID, you can use curl.
# # curl -X GET http://127.0.1:8000/items/0


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

# To start the server, run the following command in your terminal:
# uvicorn user:app --reload
# In here user is the name of the file without the .py extension 
# while app is the FastAPI instance.

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

# To test the POST endpoint, you can use curl.
# curl -X POST -H "Content-Type: application/json" -d '{"text": "apple"}' 'http://127.0.1:8000/items'


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]
# This set the default limit to 10 items.
# curl -X GET 'http://127.0.1:8000/items?limit=5'

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# To get item by ID, you can use curl.
# curl -X GET http://127.0.1:8000/items/0

########################################
# To view the API documentation, go to:
# http://127.0.0.1:8000/docs#/
########################################

