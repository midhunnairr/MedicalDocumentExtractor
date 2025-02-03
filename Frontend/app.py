import streamlit as st
import requests

# URL of the FastAPI backend (adjust the URL if necessary)
API_URL = "http://127.0.0.1:8000/extractor"


def main():
    # Set the title of the web application
    st.title("Medical Document Extractor")

    # Upload a medical PDF file
    uploaded_file = st.file_uploader("Upload a PDF medical document", type=["pdf"])

    # Select the file format for extraction (patient details or prescription)
    file_format = st.selectbox("Select the file format for extraction", ["patient_details", "prescription"])

    # If a file is uploaded and a format is selected, proceed with extraction
    if uploaded_file is not None and file_format:
        # Display file details
        st.write(f"**File Name**: {uploaded_file.name}")
        st.write(f"**File Size**: {uploaded_file.size} bytes")

        # Button to trigger the extraction
        if st.button("Extract Details"):
            # Prepare the data and file to send to FastAPI backend
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            data = {"file_format": file_format}

            # Send the file and data to the FastAPI backend
            with st.spinner("Extracting details from the document..."):
                try:
                    response = requests.post(API_URL, files=files, data=data)

                    # Handle successful response
                    if response.status_code == 200:
                        st.success("Extraction successful!")
                        extracted_data = response.json()

                        # Display the extracted data
                        st.write("**Extracted Information**:")
                        st.json(extracted_data)
                    else:
                        st.error(f"Error {response.status_code}: {response.text}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
