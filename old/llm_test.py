import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

llm = genai.Client()

context = ['INVOICE', 'LOGO', 'Saffron Design', '77 Namrata Bldg', 'Delhi, Delhi 400077', 'BILL TO', 'SHIP TO', 'INVOICE #', 'Kavindra Mannan', 'IN-001', 'Kavindra Mannan', 'INVOICEDATE', '27, DIf City, Gupta', '264,Abdul Rehman', '29/01/2019', 'Delhi, Delhi 40003', 'P.O.#', 'Mumbai, Bihar 40009', '2430/2019', 'DUE DATE', '26/04/2019', 'QTY', 'DESCRIPTION', 'UNIT PRICE', 'AMOUNT', '1', 'Frontend design restructure', '9,999.00', '9,999.00', '2', 'Custom icon package', '975.00', '1,950.00', '3', 'Gandhi mouse pad', '99.00', '297.00', 'Subtotal', '12,246.00', 'GST 12.0%', '1,469.52', 'TOTAL', '13,715.52', 'PripChopra', 'TERMS &CONDITIONS', 'Payment is due within 15 days', 'Thank you', 'State Bank of India', 'Account Number: 12345678', 'Routing Number: 09876543210']


def llm_response(context:str):
    response = llm.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="""
            You are a structured data extraction system.

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

## second iteration

# def llm_response(context:str):
#     response = llm.models.generate_content(
#         model="gemini-3-flash-preview",
#         config=types.GenerateContentConfig(
#             system_instruction="""You are a data extraction system.

#                 Extract the following fields from the input text and return ONLY valid JSON:

#                 - invoice_id (string)
#                 - customer_name (string)
#                 - date (ISO format YYYY-MM-DD or null if not present)
#                 - company_name (string)
#                 - address (string)
#                 - total_amount (number)

#                 Rules:
#                 - If a string field is missing, return "N/A".
#                 - If total_amount is missing, return 0.
#                 - If date is missing, return null.
#                 - Output must be valid JSON only. No explanations, no extra text.
#             """
#         ),
#         contents=f"{context}",
#     )
#     return response.text

print(llm_response(context))


##first iteration 

# "You are a data formatter.
# format the input data and return a json as output with following fields 
# invoice id, customer name, date, company name ,address and total amount.
# if data is not present return N/A for string fields and 0 for integer fields and none for date"