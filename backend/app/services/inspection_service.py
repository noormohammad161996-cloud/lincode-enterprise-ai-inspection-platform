from sqlalchemy.orm import Session

from app import crud, schemas


def create_inspection(
    db: Session,
    inspection: schemas.InspectionCreate,
    uploaded_filename: str,
    file_path: str,
):
    """
    Create a new inspection record.
    """

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
