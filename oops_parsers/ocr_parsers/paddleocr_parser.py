from paddleocr import PaddleOCR
from oops_parsers.parsers import AbstractParser
from logger.logger import get_logger


class PaddleOCRParser(AbstractParser):

    def __init__(self):
        self.logger = get_logger(__name__)
        self.ocr = PaddleOCR()

    def parse(self, file_path:str)->str:
        try :
            result = self.ocr.ocr(file_path)
            texts = result[0]["rec_texts"]
            return " ".join(texts)
        except Exception as e:
            self.logger.exception(f"OCR parsing failed")
            raise Exception(f"OCR parsing failed {e}")