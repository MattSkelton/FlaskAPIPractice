import uuid
from flask import Flask, request
from db import items, stores
app = Flask(__name__)


@app.get("/store")
def get_Stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_Store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id":store_id}
    stores[store_id] = new_store
    return new_store, 201

@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    item_id = uuid.uuid4().hex


@app.get("/store/<string:store_id>")
def get_Store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_StoreItems(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404