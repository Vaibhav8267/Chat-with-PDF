import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, "rb") as file:  # Open the file in binary mode
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text