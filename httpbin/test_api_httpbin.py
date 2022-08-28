import pytest


# Check request status code
@pytest.mark.regres
@pytest.mark.parametrize("code", [200, 300, 404, 500])
def test_url_status_200(base_url, code, request_method):
    target = base_url + f"{code}"
    response = request_method(url=target)
    assert response.status_code == code


@pytest.mark.regres
@pytest.mark.parametrize("code", [400])
def test_url_status_400(base_url, code, request_method):
    target = base_url + "uyuyuyuyuyuyu"
    response = request_method(url=target)
    assert response.status_code == code
