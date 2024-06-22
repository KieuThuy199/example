from fastapi import APIRouter, HTTPException
from bson import ObjectId

from database import get_collection
from models import Item, ItemInDB, serialize_items, serialize_item

route = APIRouter()
news_collection = get_collection()


@route.get("/news/", response_model=list[ItemInDB])
async def index():
    result = list(news_collection.find())
    return serialize_items(result)


@route.get("/news/{news_id}", response_model=ItemInDB | str)
async def show(news_id: str):
    item = news_collection.find_one({"_id": ObjectId(news_id)})
    if item:
        return serialize_item(item)
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@route.post("/news/", response_model=ItemInDB)
async def add(data: Item):
    item_id = news_collection.insert_one(data.dict()).inserted_id
    item = news_collection.find_one({"_id": item_id})
    return serialize_item(item)


@route.put("/news/{news_id}")
async def update(news_id: str, data: Item):
    result = news_collection.update_one({"_id": ObjectId(news_id)}, {"$set": data.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Updated item successfully"}


@route.delete("/news/{news_id}")
async def delete(news_id: str):
    result = news_collection.delete_one({"_id": ObjectId(news_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Deleted item successfully"}