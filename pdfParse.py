from PyPDF2 import PdfReader

def extract_pdf_content(file):

    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text+=page.extract_text()
    return text