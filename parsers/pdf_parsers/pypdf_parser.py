from pypdf import PdfReader
from parsers.parsers import AbstractParser
from logger.logger import get_logger


class PyPDFParser(AbstractParser):

    def __init__(self):
        self.logger = get_logger(__name__)

    def parse(self, file_path):
        try:
            texts = []

            reader = PdfReader(file_path)

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    texts.append(text)

            return " ".join(texts)

        except Exception as e:
            self.logger.error("PDF parsing failed")
            raise Exception(f"PDF parsing failed : {e}")
        

# if __name__ ==  "__main__":
#     pp =PyPDFParser()
#     print(pp.parse("/home/lokesh/Downloads/invoice-0-4.pdf"))