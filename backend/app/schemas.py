from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class InspectionCreate(BaseModel):
    """
    Create inspection request.
    """

    image_name: str

    prediction: str = "Pending"

    confidence: float = 0.0

    status: str = "Uploaded"


class InspectionResponse(BaseModel):
    """
    Inspection response.
    """

    id: int

    image_name: str

    uploaded_filename: Optional[str]

    file_path: Optional[str]

    prediction: str

    confidence: float

    status: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class UploadResponse(BaseModel):
    """
    Response after uploading image.
    """

    inspection_id: int

    original_filename: str

    uploaded_filename: str

    file_path: str

    status: str
