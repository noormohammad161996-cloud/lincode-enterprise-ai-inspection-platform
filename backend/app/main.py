import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError

from app.config import settings
from app.database import Base, engine

from app.routers import health
from app.routers import inspection


def initialize_database():
    """
    Initialize database tables with retry logic.
    """

    max_retries = 10
    retry_delay = 5

    for attempt in range(1, max_retries + 1):
        try:
            Base.metadata.create_all(bind=engine)

            print(
                "Database connection successful. "
                "Tables are ready."
            )

            return

        except OperationalError:
            print(
                f"Database is not ready yet "
                f"(attempt {attempt}/{max_retries}). "
                f"Retrying in {retry_delay}s..."
            )

            if attempt == max_retries:
                raise

            time.sleep(retry_delay)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.

    Database initialization is skipped during automated tests.
    """

    if settings.ENVIRONMENT != "testing":
        initialize_database()

    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health.router)
app.include_router(inspection.router)
