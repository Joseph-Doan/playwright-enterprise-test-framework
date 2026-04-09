from __future__ import annotations


def test_health_endpoint_returns_200_and_valid_payload(health_service):
    """
    Validate that the health endpoint is reachable and returns
    a valid success-style payload.
    """
    response = health_service.get_health()

    assert response.status == 200, (
        f"Expected 200 from /health, got {response.status}. "
        f"Body: {response.text()}"
    )

    payload = response.json()

    assert isinstance(payload, dict), (
        f"Expected JSON object response, got: {payload}"
    )

    if "status" in payload:
        assert str(payload["status"]).lower() in {"ok", "healthy", "up"}, (
            f"Unexpected status value in health payload: {payload}"
        )
    elif "message" in payload:
        assert str(payload["message"]).lower() in {"ok", "healthy", "up"}, (
            f"Unexpected message value in health payload: {payload}"
        )
    else:
        raise AssertionError(
            f"Health response missing expected key ('status' or 'message'). "
            f"Payload: {payload}"
        )