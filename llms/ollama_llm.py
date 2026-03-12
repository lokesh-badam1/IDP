from ollama import chat
from llms.llms import AbstractLlms
from logger.logger import get_logger


class OllamaGemma(AbstractLlms):

    def __init__(self):
        self.logger = get_logger(__name__)

    def chat(self,context: str):
        try:
            response = chat(
                model="gemma3",
                messages=[
                    {
                        "role": "system",
                        "content": """You are a structured data extraction system.

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
                    9. Don't add even json in start
                    10. Don't change the parameter company name
                    11. Make no typing errors
                    

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
                    """,
                    },
                    {"role": "user", "content": f"{context}"},
                ],
                format="json",
            )
            return response["message"]["content"]
        except Exception as e:
            self.logger.error(f"Ollama Gemma model failed : {e}")
            raise
