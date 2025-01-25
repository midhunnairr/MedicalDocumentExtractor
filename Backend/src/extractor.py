from pdf2image import convert_from_path
import pytesseract
from Backend.src.utils import image_processing
from Backend.src.patient_details_parser import Patient
from Backend.src.parser_prescription import Prescription
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler-24.08.0\Library\bin"


def extractor(file_path, file_format):
    text = ""
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    for page in pages:
        processed_image = image_processing(page)
        contents = pytesseract.image_to_string(processed_image)
        text += "\n" + contents

    if file_format == 'prescription':
        extracted_data = Prescription(text).parse()
        print("Prescription Data:", extracted_data)  # Debug output
        return extracted_data
    elif file_format == 'patient_details':
        extracted_data = Patient(text).parse()
        print("Patient Data:", extracted_data)  # Debug output
        return extracted_data
    else:
        raise Exception(f"Invalid File Format: {file_format} not supported")




