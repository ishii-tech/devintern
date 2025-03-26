# RAG CSV Analyser

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/<your-github-username>/<repository-name>.git
   cd <repository-name>
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

- Deploy the API on a public server or provide a build file.
- Store the code in a GitHub repository with clear setup instructions.

## Coding Guidelines

- Maintain a structured project with proper documentation.
- Include a README.md with installation and usage details.
- Ensure well-commented, modular code.
- Follow FastAPI best practices and asynchronous processing where necessary.

## Brownie Points

- Streamlit UI deployed on a free hosting platform (e.g., Heroku).
- Provide real-time chat responses with streaming.
- Offer CSV preview before processing.
- Implement efficient indexing and search for CSV data.
