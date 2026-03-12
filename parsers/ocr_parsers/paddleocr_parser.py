from paddleocr import PaddleOCR
from parsers.parsers import AbstractParser
from logger.logger import get_logger


class PaddleOCRParser(AbstractParser):

    def __init__(self):
        self.logger = get_logger(__name__)
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', enable_mkldnn=False)

    def parse(self, file_path:str)->str:
        raise Exception("Something")
        try :
            result = self.ocr.ocr(file_path)
            texts = result[0]["rec_texts"]
            print(texts)
            return " ".join(texts)
        except Exception as e:
            self.logger.exception(f"OCR parsing failed")
            raise Exception(f"OCR parsing failed {e}")