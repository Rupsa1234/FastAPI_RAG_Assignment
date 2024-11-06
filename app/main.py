# app/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Ensure the "uploads" folder exists where files will be saved
if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.post("/ingest")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file in the "uploads" directory
        file_path = os.path.join("uploads", file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        return JSONResponse(content={"message": f"File '{file.filename}' uploaded successfully!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Internal Server Error: {str(e)}"})
