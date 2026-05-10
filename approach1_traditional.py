import pytesseract
from pdf2image import convert_from_path
import re

# Tell pytesseract where Tesseract is installed on Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_fields_traditional(pdf_path: str) -> dict:
    """
    Extracts order fields from a PDF using OCR + hardcoded regex rules.
    Works well for known layouts. Breaks on unknown formats.
    """
    # Step 1: Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=300)

    # Step 2: Run OCR on the first page only
    raw_text = pytesseract.image_to_string(images[0])
    print(f"\n--- RAW OCR TEXT ({pdf_path}) ---")
    print(raw_text)

    # Step 3: Extract fields using regex — hardcoded for Layout A
    customer_id = re.search(r'Customer ID[:\s]+([A-Z0-9\-]+)', raw_text)
    po_number   = re.search(r'PO Number[:\s]+([A-Z0-9\-]+)', raw_text)
    delivery    = re.search(r'Delivery Date[:\s]+(\d{2}\.\d{2}\.\d{4})', raw_text)

    return {
        'customer_id':   customer_id.group(1) if customer_id else None,
        'po_number':     po_number.group(1)   if po_number   else None,
        'delivery_date': delivery.group(1)     if delivery    else None,
    }

# --- Run on Layout A ---
print("\n=== Layout A (Alpha GmbH) ===")
result_a = extract_fields_traditional('order_layout_a.pdf')
print("Result:", result_a)

# --- Run on Layout B ---
print("\n=== Layout B (Beta AG) ===")
result_b = extract_fields_traditional('order_layout_b.pdf')
print("Result:", result_b)