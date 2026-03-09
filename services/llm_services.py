import os
from google import genai
from google.genai import types,errors
from dotenv import load_dotenv
from logger.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")

llm = genai.Client()

def llm_response(context:str):
    try :
        response = llm.models.generate_content(
            model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(
                system_instruction="""You are a structured data extraction system.

                Extract the following fields from the input text and return ONLY valid JSON.

                Required fields:
                - invoice_id (string)
                - customer_name (string)
                - date (ISO format YYYY-MM-DD or null if not present)
                - company_name (string)
                - address (string)
                - gst_number (string)
                - total_amount (number)
                - items (array of objects)

                Items object structure:
                Each item in the items array must contain:
                - item_name (string)
                - quantity (number)
                - unit_price (number)
                - total_price (number)

                Rules:
                1. If any string field is missing, return "N/A".
                2. If gst_number is missing, return "N/A".
                3. If total_amount is missing, return 0.
                4. If date is missing, return null.
                5. If items cannot be determined, return an empty array [].
                6. Ensure numbers are returned as numeric values, not strings.
                7. Do not include any explanations or extra text.
                8. Output must be valid JSON only.

                Expected JSON format:

                {
                "invoice_id": "string",
                "customer_name": "string",
                "date": "YYYY-MM-DD or null",
                "company_name": "string",
                "address": "string",
                "gst_number": "string",
                "total_amount": number,
                "items": [
                    {
                    "item_name": "string",
                    "quantity": number,
                    "unit_price": number,
                    "total_price": number
                    }
                ]
                }
                """
            ),
            contents=f"{context}",
        )
        return response.text
    except errors.ServerError as e:
        logger.exception(f"LLM failed : Server error :{e}")
        raise
    except errors.ClientError as e:
        logger.exception(f"LLM failed : Client error :{e}")
        raise
    except errors.APIError as e:
        logger.exception(f"LLM failed : API error :{e}")
        raise
    except Exception as e:
        logger.exception(f"LLM failed : {e}")
        raise
        
