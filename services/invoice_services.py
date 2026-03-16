from datetime import datetime
from logger.logger import get_logger
from database.models import Invoice,Item
from fastapi import HTTPException,status

logger = get_logger(__name__)

def add_invoice(db,json_data):
    try:
        db_data = json_data.copy()
        items = db_data.pop("items", [])
        date_value = db_data.get("date")

        if date_value:
            db_data["date"] = datetime.strptime(date_value, "%Y-%m-%d").date()
        new_invoice = Invoice(**db_data)

        for item in items:
            new_item = Item(**item)
            new_invoice.items.append(new_item)

        db.add(new_invoice)
        db.commit()
        db.refresh(new_invoice)
    except Exception as e:
        logger.error("Database insert failed")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to store invoice")
