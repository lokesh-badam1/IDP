import pdfplumber
from logger.logger import get_logger

logger = get_logger(__name__)

def parse_pdf(file_path:str):
    try:
        texts = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                texts.append(text)
            return " ".join(texts)
    except Exception as e:
        logger.error(f"PDF parsing failed")
        raise Exception(f"PDF parsing failed : {e}")
        