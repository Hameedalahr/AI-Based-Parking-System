from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A6
import os

def generate_ticket_pdf(ticket_id, slot_id, in_time, qr_path):
    os.makedirs("tickets", exist_ok=True)
    pdf_path = f"tickets/{ticket_id}.pdf"

    c = canvas.Canvas(pdf_path, pagesize=A6)
    c.drawString(30, 360, "SMART PARKING TICKET")
    c.drawString(30, 330, f"Ticket ID: {ticket_id}")
    c.drawString(30, 310, f"Slot: {slot_id}")
    c.drawString(30, 290, f"In Time: {in_time}")
    c.drawImage(qr_path, 40, 150, width=120, height=120)
    c.save()

    return pdf_path
