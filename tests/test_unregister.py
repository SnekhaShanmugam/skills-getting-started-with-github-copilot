from src.app import activities


def test_unregister_successfully_removes_participant(client):
    activity_name = "book_club"
    email = activities[activity_name]["participants"][0]

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"{email} unregistered from {activity_name}"
    assert email not in activities[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete("/activities/unknown/signup", params={"email": "someone@example.com"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_400_when_participant_not_signed_up(client):
    response = client.delete(
        "/activities/hiking/signup",
        params={"email": "not.joined@example.com"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Participant not signed up"
