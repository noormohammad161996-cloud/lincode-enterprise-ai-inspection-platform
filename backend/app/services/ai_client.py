import requests

from app.config import settings


def get_prediction(filename: str):
    """
    Send image filename to AI Service
    and receive prediction.
    """

    response = requests.post(
        f"{settings.AI_SERVICE_URL}/predict",
        json={
            "filename": filename
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()
