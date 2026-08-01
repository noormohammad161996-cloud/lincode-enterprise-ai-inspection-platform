import os
import shutil
import uuid
from fastapi import UploadFile

# Folder where uploaded files will be stored
UPLOAD_DIRECTORY = "app/uploads"

# Allowed image extensions
ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}


def validate_image(filename: str):
    """
    Validate uploaded image extension.
    """

    extension = os.path.splitext(filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Only JPG, JPEG and PNG images are allowed."
        )


def generate_unique_filename(filename: str):
    """
    Generate unique filename.
    """

    extension = os.path.splitext(filename)[1]

    unique_name = f"{uuid.uuid4()}{extension}"

    return unique_name


def save_upload_file(file: UploadFile):
    """
    Save uploaded image into uploads folder.
    """

    validate_image(file.filename)

    filename = generate_unique_filename(file.filename)

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return filename
