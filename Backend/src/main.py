import os
from fastapi import FastAPI, UploadFile, File, Form
import uuid
from Backend.src.extractor import extractor

app = FastAPI()


@app.post("/extractor")
def extract_fields(file: UploadFile = File(...), file_format: str = Form(...)):
    try:

        uploads_dir = "C:/Users/midiy/OneDrive/Desktop/Medical Prescription Extraction/Backend/uploads/"

        contents = file.file.read()
        file_path = uploads_dir + str(uuid.uuid4()) + ".pdf"

        with open(file_path, "wb") as f:
            f.write(contents)

        data = extractor(file_path, file_format)

        if os.path.exists(file_path):
            os.remove(file_path)

        return data

    except Exception as e:
        return {"error": str(e)}
