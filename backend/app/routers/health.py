from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "application": "Lincode Enterprise DevOps",
        "version": "1.0.0"
    }
