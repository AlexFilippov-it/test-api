import json
import pytest
import requests
from jsonschema import validate
from openbrew.conftest import file_json_brew


# Check request status code
@pytest.mark.regres
@pytest.mark.parametrize("code", [200])
def test_url_status(base_url, code, request_method):
    target = base_url + "breweries/madtree-brewing-cincinnati"
    response = request_method(url=target)
    assert response.status_code == code


# Check request encoding
@pytest.mark.regres
@pytest.mark.parametrize("header", ["utf-8"])
def test_url_header(base_url, header, request_method):
    target = base_url + "breweries/madtree-brewing-cincinnati"
    response = request_method(url=target)
    assert response.encoding == header


# Comparing the answer with the scheme
@pytest.mark.smoke
def test_api_json_schema(base_url):
    res = requests.get(base_url + "breweries/madtree-brewing-cincinnati")

    schema = {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "postal_code": {"type": "number"},
        "country": {"type": "string"},
        "longitude": {"type": "number"},
        "latitude": {"type": "number"},
        "phone": {"type": "number"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }

    validate(instance=res.json(), schema=schema)

    # Save request to file
    url = base_url + "breweries/madtree-brewing-cincinnati"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    with open('response.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


# Comparing the status from file with the expected result
@pytest.mark.smoke
def test_status_request():
    file_response_brew_open = open(file_json_brew, 'r')
    jsondata_open = file_response_brew_open.read()
    obj = json.loads(jsondata_open)
    assert str(obj['city']) == "Cincinnati"
    assert str(obj['website_url'][:4]) == "http"
    assert str(obj['postal_code']) == "45209-1132"
    assert str(obj['updated_at'][:3]) == "202"
