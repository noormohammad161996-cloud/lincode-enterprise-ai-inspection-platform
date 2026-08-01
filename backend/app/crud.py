from sqlalchemy.orm import Session

from app import models, schemas


def create_inspection(
    db: Session,
    inspection: schemas.InspectionCreate,
    uploaded_filename: str,
    file_path: str,
):
    """
    Create a new inspection record.
    """

    db_inspection = models.InspectionResult(
        image_name=inspection.image_name,
        uploaded_filename=uploaded_filename,
        file_path=file_path,
        prediction=inspection.prediction,
        confidence=inspection.confidence,
        status=inspection.status,
    )

    db.add(db_inspection)
    db.commit()
    db.refresh(db_inspection)

    return db_inspection


def get_all_inspections(db: Session):
    """
    Return all inspections.
    """

    return db.query(models.InspectionResult).all()


def get_inspection_by_id(
    db: Session,
    inspection_id: int
):
    """
    Return one inspection.
    """

    return (
        db.query(models.InspectionResult)
        .filter(models.InspectionResult.id == inspection_id)
        .first()
    )


def delete_inspection(
    db: Session,
    inspection_id: int
):
    """
    Delete one inspection.
    """

    inspection = get_inspection_by_id(
        db,
        inspection_id
    )

    if inspection is None:
        return False

    db.delete(inspection)
    db.commit()

    return True
