import pytesseract
from pdf2image import convert_from_path
import ollama
import json
import re

# Tell pytesseract where Tesseract is installed on Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_fields_llm(pdf_path: str) -> dict:
    """
    Extracts order fields from a PDF using OCR + a local LLM (LLaMA 3 via Ollama).
    Layout-agnostic: no hardcoded regex patterns needed.
    """
    # Step 1: Convert PDF to image (same as before)
    images = convert_from_path(pdf_path, dpi=300)

    # Step 2: Run OCR — extract raw text
    raw_text = pytesseract.image_to_string(images[0])

    # Step 3: Send raw text to LLaMA 3 via Ollama
    prompt = f"""You are a data extraction assistant.
Extract the following fields from the order document below.
Return ONLY a valid JSON object — no explanation, no markdown, no extra text.

Required fields:
- customer_id: the customer or client identifier
- po_number: the purchase order or order reference number
- delivery_date: the requested delivery or shipment date (always format as DD.MM.YYYY)
- items: a list of ordered items with quantities

If a field cannot be found, set its value to null.

Document:
\"\"\"
{raw_text}
\"\"\"
"""

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    # Step 4: Parse the JSON from the LLM response
    raw_response = response['message']['content']

    # Clean potential markdown code fences (e.g. ```json ... ```)
    cleaned = re.sub(r'```json|```', '', raw_response).strip()

    result = json.loads(cleaned)
    return result


# --- Run on Layout A ---
print("\n=== Layout A (Alpha GmbH) ===")
result_a = extract_fields_llm('order_layout_a.pdf')
print("Result:", json.dumps(result_a, indent=2))

# --- Run on Layout B ---
print("\n=== Layout B (Beta AG) ===")
result_b = extract_fields_llm('order_layout_b.pdf')
print("Result:", json.dumps(result_b, indent=2))