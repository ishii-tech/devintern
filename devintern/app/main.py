from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from app import crud, models, schemas, database

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

class QueryRequest(BaseModel):
    file_id: str
    query: str

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_id = await crud.save_file(file)
        return {"file_id": file_id, "message": "Upload successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/files", response_model=List[schemas.File])
async def list_files():
    try:
        files = await crud.get_files()
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def query_file(request: QueryRequest):
    try:
        response = await crud.query_file(request.file_id, request.query)
        return {"response": response}
    except crud.FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/file/{file_id}")
async def delete_file(file_id: str):
    try:
        await crud.delete_file(file_id)
        return {"message": "File deleted successfully"}
    except crud.FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
