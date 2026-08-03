from sqlalchemy.orm import Session
from app import crud, schemas
from app.services.ai_client import get_prediction

def create_inspection(
    db: Session,
    inspection: schemas.InspectionCreate,
    uploaded_filename: str,
    file_path: str,
):
    """
    Create inspection after getting AI prediction.
    """

    # Call AI Service
    prediction_result = get_prediction(
        inspection.image_name
    )

    # Update inspection object
    inspection.prediction = prediction_result["prediction"]
    inspection.confidence = prediction_result["confidence"]
    inspection.status = "Completed"

    # Save into database
    return crud.create_inspection(
        db=db,
        inspection=inspection,
        uploaded_filename=uploaded_filename,
        file_path=file_path,
    )


def get_all_inspections(db: Session):
    """
    Return all inspection records.
    """

    return crud.get_all_inspections(db)


def get_inspection(
    db: Session,
    inspection_id: int,
):
    """
    Return one inspection.
    """

    return crud.get_inspection_by_id(
        db,
        inspection_id
    )


def delete_inspection(
    db: Session,
    inspection_id: int,
):
    """
    Delete one inspection.
    """

    return crud.delete_inspection(
        db,
        inspection_id
    )
