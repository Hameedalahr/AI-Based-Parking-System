# services/billing_service.py

from datetime import datetime


def calculate_amount(in_time: str, out_time: str):
    """
    Calculates parking duration and amount.
    Time format: DD-MM-YYYY HH:MM:SS
    """

    fmt = "%d-%m-%Y %H:%M:%S"

    in_dt = datetime.strptime(in_time, fmt)
    out_dt = datetime.strptime(out_time, fmt)

    duration_minutes = (out_dt - in_dt).total_seconds() / 60

    # 💰 Pricing rules (you can change later)
    if duration_minutes <= 30:
        amount = 0
    elif duration_minutes <= 60:
        amount = 30
    else:
        extra_hours = int((duration_minutes - 60) / 60) + 1
        amount = 30 + extra_hours * 20

    return {
        "duration_minutes": round(duration_minutes, 2),
        "amount": amount
    }
