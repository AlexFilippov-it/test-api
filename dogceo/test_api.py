import pytest
import cerberus
import requests
import json

# Check request status code
from dogceo.conftest import filename


@pytest.mark.smoke
@pytest.mark.parametrize("code", [200])
def test_url_status(base_url, code, request_method):
    target = base_url
    response = request_method(url=target)
    assert response.status_code == code


# Comparing the answer with the scheme
@pytest.mark.smoke
def test_api_json_schema(base_url):
    res = requests.get(base_url)

    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"},
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)

    # Save request to file
    url = base_url
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    with open('response.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


# Comparing the status from file with the expected result
@pytest.mark.smoke
def test_status_request():
    myfile = open(filename, 'r')
    jsondata = myfile.read()
    obj = json.loads(jsondata)
    assert str(obj['status']) == "success"


# Comparing the message from file with the expected result equal to .jpg
@pytest.mark.smoke
def test_message():
    file = open(filename, 'r')
    jsondatas = file.read()
    obj = json.loads(jsondatas)
    assert str(obj['message'][-4:]) == ".jpg"
