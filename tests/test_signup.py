from src.app import activities


def test_signup_successfully_adds_participant(client):
    activity_name = "hiking"
    email = "new.person@example.com"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"{email} signed up for {activity_name}"
    assert email in activities[activity_name]["participants"]


def test_signup_returns_404_for_unknown_activity(client):
    response = client.post("/activities/unknown/signup", params={"email": "someone@example.com"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_participant(client):
    activity_name = "book_club"
    existing_email = activities[activity_name]["participants"][0]

    response = client.post(f"/activities/{activity_name}/signup", params={"email": existing_email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Participant already signed up"
