import os
import uuid
import json
import shutil
from models.pydantic_schemas import InvoiceDetailsResponse
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status, Depends
from services.pipeline_services import run_pipeline
from logger.logger import get_logger
from typing import Annotated
from sqlalchemy.orm import Session
from database.database_con import Base, engine, get_db
from database.models import Invoice
from services.invoice_services import add_invoice

logger = get_logger(__name__)

Base.metadata.create_all(bind=engine)

router = APIRouter()

upload_dir = "uploads"


@router.post("/api/extract_details", response_model=InvoiceDetailsResponse)
def post_extract_details(
    db: Annotated[Session, Depends(get_db)],
    file: UploadFile = File(...),
    digitization: bool = Form(False),
):

    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported file type. Only PDF, JPEG, and PNG are allowed.",
        )

    file_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(upload_dir, file_name)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print(file.content_type)

    try:
        response = run_pipeline(file_path, digitization, file.content_type)
        json_data = json.loads(response)
        add_invoice(db,json_data)

        return json_data
    
    except ValueError as v:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not an Invoice"
        )
    except Exception as e:
        logger.exception("Pipeline processing failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process invoice",
        )


@router.get("/api/invoices", response_model=list[InvoiceDetailsResponse])
def get_invoices(db: Annotated[Session, Depends(get_db)]):
    invoices_data = db.query(Invoice).all()
    return invoices_data
