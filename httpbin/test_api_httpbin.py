import pytest


# Check request status code
@pytest.mark.regres
@pytest.mark.parametrize("code", [200])
def test_url_status_200(base_url, code, request_method):
    target = base_url + "200"
    response = request_method(url=target)
    assert response.status_code == code


@pytest.mark.regres
@pytest.mark.parametrize("code", [300])
def test_url_status_300(base_url, code, request_method):
    target = base_url + "300"
    response = request_method(url=target)
    assert response.status_code == code


@pytest.mark.regres
@pytest.mark.parametrize("code", [400])
def test_url_status_400(base_url, code, request_method):
    target = base_url + "uyuyuyuyuyuyu"
    response = request_method(url=target)
    assert response.status_code == code


@pytest.mark.regres
@pytest.mark.parametrize("code", [404])
def test_url_status_404(base_url, code, request_method):
    target = base_url + "404"
    response = request_method(url=target)
    assert response.status_code == code


@pytest.mark.regres
@pytest.mark.parametrize("code", [500])
def test_url_status_500(base_url, code, request_method):
    target = base_url + "500"
    response = request_method(url=target)
    assert response.status_code == code
