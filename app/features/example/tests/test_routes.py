from fastapi.testclient import TestClient


def test_anonymous_is_redirected_to_signin(client: TestClient) -> None:
    response = client.get("/example", follow_redirects=False)

    assert response.status_code == 303
    assert response.headers["location"] == "/auth/signin"


def test_list_page_shows_seeded_items(signed_in_client: TestClient) -> None:
    response = signed_in_client.get("/example")

    assert response.status_code == 200
    assert "First example item" in response.text


def test_create_valid_item_redirects_and_shows_it(signed_in_client: TestClient) -> None:
    response = signed_in_client.post(
        "/example",
        data={"title": "Neuer Eintrag", "description": "Aus dem Test"},
        follow_redirects=False,
    )

    assert response.status_code == 303
    assert "Neuer Eintrag" in signed_in_client.get("/example").text


def test_create_invalid_item_shows_translated_field_errors(signed_in_client: TestClient) -> None:
    response = signed_in_client.post("/example", data={"title": "", "description": ""})

    assert response.status_code == 400
    assert "Bitte geben Sie einen Titel ein." in response.text
    assert "Bitte geben Sie eine Beschreibung ein." in response.text
