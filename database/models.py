from datetime import datetime
from sqlalchemy import DateTime,Integer,String,Float
from sqlalchemy.orm import Mapped,mapped_column
from database.database_con import Base

class Invoice(Base):

    __tablename__ = "invoices"
    id : Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    invoice_id: Mapped[str] = mapped_column(String)
    customer_name: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime)
    company_name: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    gst_number: Mapped[str] = mapped_column(String)
    total_amount: Mapped[int] = mapped_column(Float)

