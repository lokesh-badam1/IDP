import pdfplumber
from parsers.parsers import AbstractParser
from logger.logger import get_logger

class PdfPlumberParser(AbstractParser):

    def __init__(self):
        self.logger = get_logger(__name__)

    def parse(self, file_path):
        try:
            texts = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    texts.append(text)
                return " ".join(texts)
        except Exception as e:
            self.logger.error(f"PDF parsing failed")
            raise Exception(f"PDF parsing failed : {e}")