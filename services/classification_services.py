import os
from google import genai
from dotenv import load_dotenv
from logger.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")

llm = genai.Client()


def classify_document(text: str):
    prompt = f"""
    Determine if the following document is an invoice.
    Answer only with: INVOICE or NOT_INVOICE.

    Document text:
    {text}
    """


    response = llm.models.generate_content(
            model="gemini-3-flash-preview",contents=prompt)
    return response.text.strip()