def test_feedback_form_shows_validation_errors(client):
    response = client.post("/feedback", data={
        "name": "",
        "email": "not-an-email",
        "topic": "",
        "message": "too short",
    })

    assert response.status_code == 200
    assert b"field-error" in response.data


def test_feedback_form_success_redirects(client):
    response = client.post("/feedback", data={
        "name": "Ari",
        "email": "ari@example.com",
        "topic": "Question",
        "message": "This message is long enough.",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"received your feedback" in response.data