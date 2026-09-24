from app import app


# TC-AUTO-001
# Verify GET all patients returns HTTP 200.
def test_get_all_patients():
    client = app.test_client()

    response = client.get("/api/patients")

    assert response.status_code == 200


# TC-AUTO-002
# Verify Patient ID 1 returns Jordan Smith.
def test_get_patient_by_id():
    client = app.test_client()

    response = client.get("/api/patients/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["first_name"] == "Jordan"
    assert data["last_name"] == "Smith"


# TC-AUTO-003
# Verify nonexistent patient returns HTTP 404.
def test_patient_not_found():
    client = app.test_client()

    response = client.get("/api/patients/999")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Patient not found"


# TC-AUTO-004
# Verify a new patient can be created.
def test_create_patient():
    client = app.test_client()

    new_patient = {
        "first_name": "Automation",
        "last_name": "Tester",
        "date_of_birth": "1994-06-15",
        "phone": "555-0707",
        "email": "automation.tester@example.com"
    }

    response = client.post(
        "/api/patients",
        json=new_patient
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["first_name"] == "Automation"
    assert data["last_name"] == "Tester"
    assert data["email"] == "automation.tester@example.com"


# TC-AUTO-005
# Verify missing required field returns HTTP 400.
def test_missing_required_field():
    client = app.test_client()

    patient = {
        "first_name": "Casey",
        "last_name": "Wilson",
        "date_of_birth": "1995-07-18",
        "phone": "555-0404"
    }

    response = client.post(
        "/api/patients",
        json=patient
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "All patient fields are required"


# TC-AUTO-006
# Verify empty required field returns HTTP 400.
def test_empty_required_field():
    client = app.test_client()

    patient = {
        "first_name": "Jamie",
        "last_name": "Lee",
        "date_of_birth": "1993-11-05",
        "phone": "555-0505",
        "email": ""
    }

    response = client.post(
        "/api/patients",
        json=patient
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "All patient fields are required"