import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

import cv2
from pyzbar.pyzbar import decode
from services.exit_service import close_ticket
from services.billing_service import calculate_amount
from config.firebase_init import db


def run_exit_scanner():
    cap = cv2.VideoCapture(0)
    scanned_ticket = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for qr in decode(frame):
            scanned_ticket = qr.data.decode("utf-8")
            cap.release()
            cv2.destroyAllWindows()
            break

        cv2.imshow("Exit Scanner - Show QR", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    if not scanned_ticket:
        return {"error": "No QR scanned"}

    ticket_ref = db.collection("tickets").document(scanned_ticket)
    ticket_doc = ticket_ref.get()

    if not ticket_doc.exists:
        return {"error": "Invalid ticket"}

    ticket = ticket_doc.to_dict()

    close_info = close_ticket(scanned_ticket)
    bill = calculate_amount(
        ticket["in_time"],
        close_info["out_time"].strftime("%d-%m-%Y %H:%M:%S")
    )

    return {
        "message": "Gate opened",
        "bill": bill,
        "slot_id": ticket["slot_id"]
    }
