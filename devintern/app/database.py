from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import os

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.rag_csv_analyser
files_collection = database.get_collection("files")

async def connect():
    client.admin.command('ping')

async def disconnect():
    client.close()
