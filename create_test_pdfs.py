from fpdf import FPDF

# ---- PDF Layout A: Alpha GmbH (standard field names) ----
pdf_a = FPDF()
pdf_a.add_page()
pdf_a.set_font("Helvetica", size=12)

pdf_a.cell(200, 10, txt="Order form", new_x="LMARGIN", new_y="NEXT", align="C")
pdf_a.ln(10)
pdf_a.cell(200, 10, txt="Alpha GmbH", new_x="LMARGIN", new_y="NEXT")
pdf_a.cell(200, 10, txt="Customer ID: C-1042", new_x="LMARGIN", new_y="NEXT")
pdf_a.cell(200, 10, txt="PO Number: PO-88321", new_x="LMARGIN", new_y="NEXT")
pdf_a.cell(200, 10, txt="Delivery Date: 15.04.2025", new_x="LMARGIN", new_y="NEXT")
pdf_a.ln(5)
pdf_a.cell(200, 10, txt="Items:", new_x="LMARGIN", new_y="NEXT")
pdf_a.cell(200, 10, txt="  - 50x Product A", new_x="LMARGIN", new_y="NEXT")
pdf_a.cell(200, 10, txt="  - 20x Product B", new_x="LMARGIN", new_y="NEXT")

pdf_a.output("order_layout_a.pdf")
print("order_layout_a.pdf created.")

# ---- PDF Layout B: Beta AG (different field names and date format) ----
pdf_b = FPDF()
pdf_b.add_page()
pdf_b.set_font("Helvetica", size=12)

pdf_b.cell(200, 10, txt="ORDER FORM", new_x="LMARGIN", new_y="NEXT", align="C")
pdf_b.ln(10)
pdf_b.cell(200, 10, txt="Beta AG", new_x="LMARGIN", new_y="NEXT")
pdf_b.cell(200, 10, txt="Order Reference: ORD-99210", new_x="LMARGIN", new_y="NEXT")
pdf_b.cell(200, 10, txt="Client Code: B-2077", new_x="LMARGIN", new_y="NEXT")
pdf_b.cell(200, 10, txt="Requested Delivery: April 20, 2025", new_x="LMARGIN", new_y="NEXT")
pdf_b.ln(5)
pdf_b.cell(200, 10, txt="Order Details:", new_x="LMARGIN", new_y="NEXT")
pdf_b.cell(200, 10, txt="  Product X (qty: 10)", new_x="LMARGIN", new_y="NEXT")
pdf_b.cell(200, 10, txt="  Product Y (qty: 5)", new_x="LMARGIN", new_y="NEXT")

pdf_b.output("order_layout_b.pdf")
print("order_layout_b.pdf created.")