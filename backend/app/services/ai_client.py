import requests

AI_SERVICE_URL = "http://127.0.0.1:8001/predict"


def get_prediction(filename: str):
    """
    Send filename to AI Service
    and receive prediction.
    """

    response = requests.post(
        AI_SERVICE_URL,
        json={
            "filename": filename
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()
