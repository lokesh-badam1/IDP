from paddleocr import PaddleOCR
from logger.logger import get_logger

logger = get_logger(__name__)
ocr = PaddleOCR()


def parse_ocr(file_path:str):
    try :
        result = ocr.ocr(file_path)
        texts = result[0]["rec_texts"]
        return " ".join(texts)
    except Exception as e:
        logger.exception(f"OCR parsing failed: {e}")
        raise


