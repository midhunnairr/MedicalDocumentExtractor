import os
from fastapi import FastAPI, UploadFile, File, Form
import uuid
from Backend.src.extractor import extractor

app = FastAPI()

# Define the uploads directory
uploads_dir = "C:/Users/midiy/OneDrive/Desktop/MedicalDocumentExtractor/Backend/uploads/"

# Ensure the uploads directory exists
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

@app.post("/extractor")
def extract_fields(file: UploadFile = File(...), file_format: str = Form(...)):
    try:
        # Read file contents
        contents = file.file.read()

        # Generate a unique file path using os.path.join for safe path handling
        file_path = os.path.join(uploads_dir, str(uuid.uuid4()) + ".pdf")

        # Log the file path for debugging (optional)
        print(f"Saving file to: {file_path}")

        # Save the uploaded file to disk
        with open(file_path, "wb") as f:
            f.write(contents)

        # Call the extractor function to process the file
        data = extractor(file_path, file_format)

        # Remove the file after processing
        if os.path.exists(file_path):
            os.remove(file_path)

        return data

    except Exception as e:
        # Return error message if something goes wrong
        return {"error": str(e)}
