def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_activity_mapping(client):
    response = client.get("/activities")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "hiking" in data
    assert "participants" in data["hiking"]
