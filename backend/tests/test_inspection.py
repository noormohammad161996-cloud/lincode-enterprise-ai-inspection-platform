from app import crud, schemas


def test_create_inspection(db):
    inspection = schemas.InspectionCreate(
        image_name="bearing-good-01.jpg",
        prediction="Good",
        confidence=98.76,
        status="Completed",
    )

    created = crud.create_inspection(
        db=db,
        inspection=inspection,
        uploaded_filename="test-bearing.jpg",
        file_path="app/uploads/test-bearing.jpg",
    )

    assert created.id is not None
    assert created.image_name == "bearing-good-01.jpg"
    assert created.uploaded_filename == "test-bearing.jpg"
    assert created.file_path == "app/uploads/test-bearing.jpg"
    assert created.prediction == "Good"
    assert created.confidence == 98.76
    assert created.status == "Completed"


def test_get_all_inspections(db):
    inspection = schemas.InspectionCreate(
        image_name="bearing-test.jpg",
        prediction="Good",
        confidence=95.50,
        status="Completed",
    )

    crud.create_inspection(
        db=db,
        inspection=inspection,
        uploaded_filename="bearing-test.jpg",
        file_path="app/uploads/bearing-test.jpg",
    )

    results = crud.get_all_inspections(db)

    assert len(results) == 1
    assert results[0].image_name == "bearing-test.jpg"


def test_get_inspection_by_id(db):
    inspection = schemas.InspectionCreate(
        image_name="bearing-id-test.jpg",
        prediction="Good",
        confidence=97.25,
        status="Completed",
    )

    created = crud.create_inspection(
        db=db,
        inspection=inspection,
        uploaded_filename="bearing-id-test.jpg",
        file_path="app/uploads/bearing-id-test.jpg",
    )

    result = crud.get_inspection_by_id(
        db,
        created.id,
    )

    assert result is not None
    assert result.id == created.id
    assert result.image_name == "bearing-id-test.jpg"


def test_get_inspection_by_id_not_found(db):
    result = crud.get_inspection_by_id(
        db,
        99999,
    )

    assert result is None


def test_delete_inspection(db):
    inspection = schemas.InspectionCreate(
        image_name="bearing-delete-test.jpg",
        prediction="Good",
        confidence=99.10,
        status="Completed",
    )

    created = crud.create_inspection(
        db=db,
        inspection=inspection,
        uploaded_filename="bearing-delete-test.jpg",
        file_path="app/uploads/bearing-delete-test.jpg",
    )

    deleted = crud.delete_inspection(
        db,
        created.id,
    )

    assert deleted is True

    result = crud.get_inspection_by_id(
        db,
        created.id,
    )

    assert result is None


def test_delete_inspection_not_found(db):
    deleted = crud.delete_inspection(
        db,
        99999,
    )

    assert deleted is False


def test_upload_image_success(client, monkeypatch, tmp_path):
    """
    Test the complete image upload flow.

    The real AI service is mocked so this test
    does not depend on another running container.
    """

    monkeypatch.setattr(
        "app.routers.inspection.save_upload_file",
        lambda file: "test-upload.jpg",
    )

    monkeypatch.setattr(
        "app.services.inspection_service.get_prediction",
        lambda filename: {
            "prediction": "Good",
            "confidence": 98.76,
        },
    )

    response = client.post(
        "/api/v1/inspection/upload",
        files={
            "file": (
                "bearing-good-01.jpg",
                b"fake-image-content",
                "image/jpeg",
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["inspection_id"] == 1
    assert data["original_filename"] == "bearing-good-01.jpg"
    assert data["uploaded_filename"] == "test-upload.jpg"
    assert data["file_path"] == "app/uploads/test-upload.jpg"
    assert data["status"] == "Completed"


def test_upload_image_invalid_extension(client):
    """
    Unsupported file extensions should return HTTP 400.
    """

    response = client.post(
        "/api/v1/inspection/upload",
        files={
            "file": (
                "malicious.txt",
                b"not-an-image",
                "text/plain",
            )
        },
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == (
        "Only JPG, JPEG and PNG images are allowed."
    )
