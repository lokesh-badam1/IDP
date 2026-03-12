from IDP.old.paddle_services_test import parse_ocr
from IDP.old.pdf_services_test import parse_pdf
from services.llm_services import llm_response
from parsers.ocr_parsers.paddleocr_parser import PaddleOCRParser
from parsers.pdf_parsers.pdfplummer_parser import PdfPlumberParser
from services.ollama_services import ollama_response
from services.classification_services import classify_document

from logger.logger import get_logger

logger = get_logger(__name__)

# def run_pipeline(filepath:str,digitization:bool):

def oops_ocr_pipeline(file_path:str):
    try:
        logger.info("Starting OCR")

        parser = PaddleOCRParser()
        ocr_output = parser.parse(file_path)

        logger.info("Completed OCR")

        classification_result = classify_document(ocr_output)
        if classification_result != "INVOICE":
            raise ValueError("Uploaded document is not an invoice")

        logger.info("Starting LLM Processing")

        # llm_output = llm_response(ocr_output)
        llm_output = ollama_response(ocr_output)

        logger.info("Completed LLM Processing")
        # print(llm_output)
        return llm_output
    except ValueError as v:
        logger.exception(f"Not a invoice")
        raise v
    except Exception:
        logger.exception(f"OCR pipeline failed")

def ocr_pipeline(file_path:str):
    try:
        logger.info("Starting OCR")

        ocr_output = (file_path)

        logger.info("Completed OCR")
        logger.info("Starting LLM Processing")

        llm_output = llm_response(ocr_output)

        logger.info("Completed LLM Processing")
        # print(llm_output)
        return llm_output
    except Exception:
        logger.exception(f"OCR pipeline failed")
        

def pdf_pipeline(file_path:str):
    try :
        logger.info("Starting PDF Parsing")

        pdf_output =  parse_pdf(file_path)

        logger.info("Completed PDF Parsing")
        logger.info("Starting LLM Processing")

        llm_output = llm_response(pdf_output)

        logger.info("Completed LLM Processing")
        # print(llm_output)
        return llm_output
    except Exception:
        logger.exception(f"PDF pipeline failed")

def oops_pdf_pipeline(file_path:str):
    try :
        logger.info("Starting PDF Parsing")

        parser = PdfPlumberParser()
        pdf_output = parser.parse(file_path)
        # pdf_output =  parse_pdf(file_path)

        logger.info("Completed PDF Parsing")
        logger.info("Starting LLM Processing")

        llm_output = llm_response(pdf_output)

        logger.info("Completed LLM Processing")
        # print(llm_output)
        return llm_output
    except Exception:
        logger.exception(f"PDF pipeline failed")


def run_pipeline(file_path,digitization,content_type:str):
    if content_type == "application/pdf" and digitization == False:
        return oops_pdf_pipeline(file_path)
    elif content_type == "application/pdf" and digitization == True:
        return oops_ocr_pipeline(file_path)
    elif content_type == "image/jpeg" or content_type =="image/png":
        return oops_ocr_pipeline(file_path)
