import uuid
from datetime import datetime
from config.firebase_init import db
import qrcode
import os

def generate_ticket():
    # Find free slot
    for s in db.collection("slots").stream():
        if not s.to_dict().get("occupied", False):
            slot_id = s.id
            break
    else:
        return None

    ticket_id = str(uuid.uuid4())[:8]
    in_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Lock slot
    db.collection("slots").document(slot_id).update({
        "occupied": True,
        "locked": True
    })

    # Save ticket
    db.collection("tickets").document(ticket_id).set({
        "slot_id": slot_id,
        "in_time": in_time,
        "status": "ACTIVE"
    })

    # QR
    os.makedirs("qr_codes", exist_ok=True)
    qr_path = f"qr_codes/{ticket_id}.png"
    qrcode.make(ticket_id).save(qr_path)

    return {
        "ticket_id": ticket_id,
        "slot_id": slot_id,
        "in_time": in_time,
        "qr_path": qr_path
    }
