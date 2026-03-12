import pytesseract
from PIL import Image
from parsers.parsers import AbstractParser
from logger.logger import get_logger


class TesseractOCRParser(AbstractParser):

    def __init__(self):
        self.logger = get_logger(__name__)

    def parse(self, file_path: str) -> str:
        try:
            image = Image.open(file_path)

            text = pytesseract.image_to_string(image)

            return text.strip()

        except Exception as e:
            self.logger.exception("OCR parsing failed")
            raise Exception(f"OCR parsing failed {e}")
        
# if __name__ == "__main__":
#     pp = TesseractOCRParser()
#     print(pp.parse("/home/lokesh/Downloads/inv.png"))