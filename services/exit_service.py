from datetime import datetime
from config.firebase_init import db

def close_ticket(ticket_id):
    ticket_ref = db.collection("tickets").document(ticket_id)
    ticket = ticket_ref.get().to_dict()

    slot_id = ticket["slot_id"]

    ticket_ref.update({
        "status": "CLOSED",
        "out_time": datetime.now()
    })

    db.collection("slots").document(slot_id).update({
        "occupied": False,
        "locked": False
    })

    return {"slot_id": slot_id}
