import sys, os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from config.firebase_init import db
from services.ticket_service import generate_ticket
from services.exit_service import close_ticket
from services.pdf_ticket_service import generate_ticket_pdf
from services.email_service import send_ticket_email

app = FastAPI()

# Static files
app.mount("/web", StaticFiles(directory=os.path.join(PROJECT_ROOT, "web")), name="web")
app.mount("/tickets", StaticFiles(directory=os.path.join(PROJECT_ROOT, "tickets")), name="tickets")

# ---------- MODELS ----------
class TicketReq(BaseModel):
    email: str

class ReleaseReq(BaseModel):
    ticket_id: str


# ---------- SLOT STATUS ----------
@app.get("/slots/status")
def slot_status():
    total, free = 0, 0
    for s in db.collection("slots").stream():
        total += 1
        if not s.to_dict().get("occupied", False):
            free += 1
    return {"free_slots": free, "total_slots": total}


# ---------- DEMO: CAR PARKED ----------
@app.post("/demo/car-parked")
def demo_car_parked():
    for s in db.collection("slots").stream():
        if not s.to_dict().get("occupied", False):
            db.collection("slots").document(s.id).update({"occupied": True})
            return {"occupied_slot": s.id}
    return {"error": "No free slots"}


# ---------- GENERATE TICKET ----------
@app.post("/ticket/generate")
def generate_ticket_api(req: TicketReq):
    ticket = generate_ticket()
    if not ticket:
        return {"error": "No slots available"}

    pdf_path = generate_ticket_pdf(
        ticket["ticket_id"],
        ticket["slot_id"],
        ticket["in_time"],
        ticket["qr_path"]
    )

    send_ticket_email(req.email, pdf_path)

    return {
        "ticket_id": ticket["ticket_id"],
        "slot_id": ticket["slot_id"],
        "in_time": ticket["in_time"]
    }


# ---------- RELEASE TICKET ----------
@app.post("/ticket/release")
def release_ticket(req: ReleaseReq):
    close_ticket(req.ticket_id)
    return {"message": "Slot released"}
@app.post("/admin/reset-slots")
def reset_slots():
    slots = db.collection("slots").stream()
    for s in slots:
        db.collection("slots").document(s.id).update({
            "occupied": False,
            "locked": False
        })
    return {"message": "All slots reset"}
