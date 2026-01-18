from config.firebase_init import db

def reset_all_slots():
    slots = db.collection("slots").stream()
    count = 0

    for s in slots:
        db.collection("slots").document(s.id).update({
            "occupied": False,
            "locked": False
        })
        count += 1

    print(f"✅ Reset {count} slots to free")

if __name__ == "__main__":
    reset_all_slots()
