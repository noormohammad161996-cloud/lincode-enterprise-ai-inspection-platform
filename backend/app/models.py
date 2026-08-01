from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from app.database import Base


class InspectionResult(Base):
    """
    Stores AI inspection results.
    """

    __tablename__ = "inspection_results"

    id = Column(Integer, primary_key=True, index=True)

    image_name = Column(String(255), nullable=False)

    uploaded_filename = Column(String(255), nullable=True)

    file_path = Column(String(500), nullable=True)

    prediction = Column(String(100), nullable=False)

    confidence = Column(Float, nullable=False)

    status = Column(String(50), default="Completed")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
