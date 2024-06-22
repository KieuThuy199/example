from pydantic import BaseModel, Field
from typing import Union

import datetime


class Item(BaseModel):
    title: str
    author: str
    avatar: Union[str, None] = None
    avatar_desc: Union[str, None] = None
    sapo: Union[str, None] = None
    content: str
    scraped_time: datetime.datetime = Field(default_factory=datetime.datetime.now)


class ItemInDB(Item):
    id: str


def serialize_item(item: Item):
    item["id"] = str(item["_id"])
    item.pop("_id")
    return item


def serialize_items(items: list[Item]) -> list:
    return [serialize_item(item) for item in items]
