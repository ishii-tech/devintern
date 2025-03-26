from app.database import files_collection
from app.models import File
from bson.objectid import ObjectId
from fastapi import UploadFile
import csv
import io

class FileNotFoundError(Exception):
    pass

async def save_file(file: UploadFile) -> str:
    content = await file.read()
    document = content.decode("utf-8")
    file_data = {
        "file_name": file.filename,
        "document": document
    }
    result = await files_collection.insert_one(file_data)
    return str(result.inserted_id)

async def get_files():
    files = await files_collection.find().to_list(100)
    return [File(file_id=str(file["_id"]), file_name=file["file_name"], document=file["document"]) for file in files]

async def query_file(file_id: str, query: str) -> str:
    file = await files_collection.find_one({"_id": ObjectId(file_id)})
    if not file:
        raise FileNotFoundError
    # Implement query logic here
    return "Query response"

async def delete_file(file_id: str):
    result = await files_collection.delete_one({"_id": ObjectId(file_id)})
    if result.deleted_count == 0:
        raise FileNotFoundError
