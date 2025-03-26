structure

── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── crud.py
│   ├── schemas.py
│   └── utils.py
├── requirements.txt
└── README.md


# RAG CSV Analyser

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/<ishii-tech>/<repository-name>.git
   cd <https://github.com/ishii-tech/devintern.git>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the app:
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `POST /upload`
  - Input: CSV file (multipart/form-data) or file path (JSON body)
  - Output: `{ "file_id": "string", "message": "Upload successful" }`
  - Errors: 400 Bad Request if file format is invalid, 500 Internal Server Error for storage issues.

- `GET /files`
  - Input: None
  - Output: `{ "files": [{ "file_id": "string", "file_name": "string" }] }`
  - Errors: 500 Internal Server Error if retrieval fails.

- `POST /query`
  - Input: `{ "file_id": "string", "query": "string" }`
  - Output: `{ "response": "string" }`
  - Errors: 404 Not Found if file not found, 400 Bad Request for missing parameters.

- `DELETE /file/{file_id}`
  - Input: File ID (URL parameter)
  - Output: `{ "message": "File deleted successfully" }`
  - Errors: 404 Not Found if file does not exist, 500 Internal Server Error for deletion failure.

## Deployment Notes

1. **Project Structure**:
   - The project is organized into several files and directories to maintain a clean and modular structure.
   - The main application logic is in the `app` directory, which contains submodules for models, database connections, CRUD operations, and schemas.

2. **Database**:
   - MongoDB is used as the NoSQL database to store CSV files and their metadata.
   - The `motor` library is used for asynchronous interaction with MongoDB.

3. **API Endpoints**:
   - `POST /upload`: Uploads a CSV file and stores it in the database.
   - `GET /files`: Lists all uploaded CSV files.
   - `POST /query`: Queries a specific CSV file based on the provided query.
   - `DELETE /file/{file_id}`: Deletes a specific CSV file from the database.

4. **Error Handling**:
   - Proper error handling is implemented to return appropriate status codes and error messages for different scenarios.

### How to Execute the Solution

1. **Clone the Repository**:
   - Clone the repository from GitHub to your local machine.
   ```sh
   git clone https://github.com/<your-github-username>/<repository-name>.git
   cd <repository-name>
   ```

2. **Install Dependencies**:
   - Install the required dependencies using `pip`.
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB**:
   - Ensure that MongoDB is installed and running on your local machine or a remote server.
   - Update the `MONGO_DETAILS` environment variable in `app/database.py` if necessary.

4. **Run the Application**:
   - Start the FastAPI application using `uvicorn`.
   ```sh
   uvicorn app.main:app --reload
   ```

5. **API Endpoints**:
   - Use the following endpoints to interact with the API:

   - `POST /upload`:
     - Input: CSV file (multipart/form-data) or file path (JSON body)
     - Output: `{ "file_id": "string", "message": "Upload successful" }`
     - Errors: 400 Bad Request if file format is invalid, 500 Internal Server Error for storage issues.

   - `GET /files`:
     - Input: None
     - Output: `{ "files": [{ "file_id": "string", "file_name": "string" }] }`
     - Errors: 500 Internal Server Error if retrieval fails.

   - `POST /query`:
     - Input: `{ "file_id": "string", "query": "string" }`
     - Output: `{ "response": "string" }`
     - Errors: 404 Not Found if file not found, 400 Bad Request for missing parameters.

   - `DELETE /file/{file_id}`:
     - Input: File ID (URL parameter)
     - Output: `{ "message": "File deleted successfully" }`
     - Errors: 404 Not Found if file does not exist, 500 Internal Server Error for deletion failure.



