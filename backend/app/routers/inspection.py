from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import inspection_service
from app.utils.file_handler import save_upload_file


router = APIRouter(
    prefix="/api/v1/inspection",
    tags=["Inspection"]
)


@router.post("/", response_model=schemas.InspectionResponse)
def create_inspection(
    inspection: schemas.InspectionCreate,
    db: Session = Depends(get_db)
):
    raise HTTPException(
        status_code=501,
        detail="Use /api/v1/inspection/upload to create inspections."
    )


@router.get("/", response_model=list[schemas.InspectionResponse])
def get_all_inspections(
    db: Session = Depends(get_db)
):
    """
    Return all inspection records.
    """

    return inspection_service.get_all_inspections(db)


@router.get("/{inspection_id}", response_model=schemas.InspectionResponse)
def get_inspection(
    inspection_id: int,
    db: Session = Depends(get_db)
):
    """
    Return one inspection by ID.
    """

    inspection = inspection_service.get_inspection(
        db,
        inspection_id
    )

    if inspection is None:
        raise HTTPException(
            status_code=404,
            detail="Inspection not found"
        )

    return inspection


@router.delete("/{inspection_id}")
def delete_inspection(
    inspection_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an inspection.
    """

    deleted = inspection_service.delete_inspection(
        db,
        inspection_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Inspection not found"
        )

    return {
        "message": "Inspection deleted successfully"
    }


@router.post(
    "/upload",
    response_model=schemas.UploadResponse
)
def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload an inspection image and create
    a database record.
    """

    try:
        # Save uploaded file
        saved_filename = save_upload_file(file)

        # Relative file path stored in database
        file_path = f"app/uploads/{saved_filename}"

        # Create inspection request
        inspection = schemas.InspectionCreate(
            image_name=file.filename,
            prediction="Pending",
            confidence=0.0,
            status="Uploaded"
        )

        # Save inspection record
        inspection_record = (
            inspection_service.create_inspection(
                db=db,
                inspection=inspection,
                uploaded_filename=saved_filename,
                file_path=file_path,
            )
        )

        return schemas.UploadResponse(
            inspection_id=inspection_record.id,
            original_filename=file.filename,
            uploaded_filename=saved_filename,
            file_path=file_path,
            status=inspection_record.status,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
