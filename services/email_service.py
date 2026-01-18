import smtplib, os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_ticket_email(to_email, pdf_path):
    sender = os.getenv("GMAIL_SENDER")
    pwd = os.getenv("GMAIL_APP_PASSWORD")

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to_email
    msg["Subject"] = "Smart Parking Ticket"
    msg.set_content("Your parking ticket is attached.")

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path)
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(sender, pwd)
        s.send_message(msg)
