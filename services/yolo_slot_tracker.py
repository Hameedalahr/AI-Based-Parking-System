import cv2
import json
import numpy as np
from shapely.geometry import Polygon, box
from ultralytics import YOLO
from config.firebase_init import db

VIDEO_PATH = "data/video/CCTV_Video_of_Multiple_Vehicles.mp4"
SLOT_JSON = "data/annotations/vgg.json"

VIDEO_W, VIDEO_H = 1280, 720

# Load YOLO
model = YOLO("yolov8n.pt")

# ---------------- LOAD SLOT POLYGONS ----------------
def load_slots():
    with open(SLOT_JSON) as f:
        data = json.load(f)

    slots = []
    regions = list(data.values())[0]["regions"]

    for r in regions.values():
        xs = r["shape_attributes"]["all_points_x"]
        ys = r["shape_attributes"]["all_points_y"]

        poly = Polygon(zip(xs, ys))
        slot_id = f"slot_{r['region_attributes']['label']}"

        slots.append({
            "slot_id": slot_id,
            "polygon": poly
        })

    return slots


slots = load_slots()


# ---------------- SLOT TRACKER ----------------
def run_slot_tracker():
    cap = cv2.VideoCapture(VIDEO_PATH)
    assert cap.isOpened(), "Video not opened"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (VIDEO_W, VIDEO_H))

        results = model(frame, conf=0.4, verbose=False)[0]

        vehicle_boxes = []
        for b in results.boxes.data:
            x1, y1, x2, y2, conf, cls = b.tolist()
            if int(cls) in [2, 3, 5, 7]:  # car, bus, truck, bike
                vehicle_boxes.append(box(x1, y1, x2, y2))

        for slot in slots:
            occupied = False
            for vbox in vehicle_boxes:
                if slot["polygon"].intersection(vbox).area / slot["polygon"].area > 0.15:
                    occupied = True
                    break

            db.collection("slots").document(slot["slot_id"]).set({
                "occupied": occupied
            }, merge=True)

    cap.release()
