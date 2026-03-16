from llms.gemini_llm import Gemini
from parsers.ocr_parsers.paddleocr_parser import PaddleOCRParser
from parsers.ocr_parsers.tesseractocr_parser import TesseractOCRParser
from parsers.pdf_parsers.pdfplummer_parser import PdfPlumberParser
from parsers.pdf_parsers.pypdf_parser import PyPDFParser
from parsers.parsers import AbstractParser
from parsers.parser_router import ParserRouter
from services.classification_services import classify_document
from logger.logger import get_logger


logger = get_logger(__name__)

def pipeline(file_path:str,parsers):

    parser_output = run_parser(file_path,parsers)

    verify_invoice(parser_output)

    llm_response = run_llm(parser_output)

    return llm_response


def run_pipeline(file_path, digitization, content_type: str):
    if content_type == "application/pdf" and digitization == False:
        return pipeline(file_path,[PdfPlumberParser(),PyPDFParser()])
    elif content_type == "application/pdf" and digitization == True:
        return pipeline(file_path,[PaddleOCRParser()])
    elif content_type == "image/jpeg" or content_type == "image/png":
        return pipeline(file_path,[PaddleOCRParser(),TesseractOCRParser()])


def run_parser(file_path:str,parsers:list[AbstractParser]):
    logger.info("Starting Parser")

    router = ParserRouter(parsers)

    pdf_output = router.parse(file_path)
    
    logger.info("Parser Completed")
    return pdf_output


def verify_invoice(ocr_output:str):
    logger.info("Checking if uploaded document is an invoice")

    classification_result = classify_document(ocr_output)
    if classification_result != "INVOICE":
        raise ValueError("Uploaded document is not an invoice")
    

def run_llm(ocr_output:str)-> str:
    logger.info("Starting Gemini Llm")

    try:
        llm = Gemini()
        llm_response = llm.chat(ocr_output)
    except:
        logger.info("All LLM's Failed")
    logger.info("LLM completed")
    return llm_response


