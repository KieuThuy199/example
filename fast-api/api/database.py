from pymongo import MongoClient

MONGO_URI = 'mongodb://mongodb:27017/vtv_news_db_dev'
MONGO_DB = 'vtv_news_db_dev'
STORING_COLLECTION = 'thegioi_news'


def get_db():
    client = MongoClient(MONGO_URI)
    return client[MONGO_DB]


def get_collection():
    db = get_db()
    return db[STORING_COLLECTION]