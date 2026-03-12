from datetime import datetime

from pydantic import BaseModel, Field


class Item(BaseModel):
    item_name: str
    quantity: int
    unit_price: float
    total_price: float


class InvoiceDetailsResponse(BaseModel):
    invoice_id: str
    customer_name: str
    date: datetime | None
    company_name: str
    address: str
    gst_number: str
    total_amount: float
    items: list[Item] = Field(default_factory=list)