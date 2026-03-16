from __future__ import annotations
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey,Integer,String,Float
from sqlalchemy.orm import Mapped,mapped_column,relationship
from database.database_con import Base

class Invoice(Base):

    __tablename__ = "invoices_db"
    id : Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    invoice_id: Mapped[str] = mapped_column(String)
    customer_name: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime,nullable=True)
    company_name: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    gst_number: Mapped[str] = mapped_column(String)
    total_amount: Mapped[int] = mapped_column(Float,nullable=True)
    items: Mapped[list["Item"]] = relationship(back_populates="invoice")

class Item(Base):

    __tablename__ = "items_db"
    id : Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    item_name:Mapped[str] = mapped_column(String,nullable=True)
    quantity: Mapped[int] = mapped_column(Integer,nullable=True)
    unit_price: Mapped[float] = mapped_column(Float,nullable=True)
    total_price: Mapped[float] = mapped_column(Float,nullable=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices_db.id"))
    invoice: Mapped["Invoice"] = relationship(back_populates="items")


