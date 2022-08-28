import json
import pytest
import requests
import cerberus
from jsonplaceholder.conftest import file_json_placeholder


# Check request status code
@pytest.mark.regres
@pytest.mark.parametrize("code", [200])
def test_url_status(base_url, code, request_method):
    target = base_url + "/todos/1"
    response = request_method(url=target)
    assert response.status_code == code


# Check request encoding
@pytest.mark.regres
@pytest.mark.parametrize("header", ["utf-8"])
def test_url_header(base_url, header, request_method):
    target = base_url + "/todos/1"
    response = request_method(url=target)
    assert response.encoding == header


# Comparing the answer with the scheme
@pytest.mark.regres
def test_api_json_schema(base_url):
    res = requests.get(base_url + "/todos/1")

    schema = {
        "id": {"type": "number"},
        "userId": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)

    # Save request to file
    url = base_url + "/todos/1"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    with open('response.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


# Comparing the status from file with the expected result
@pytest.mark.smoke
def test_status_request():
    file_response_placeholder = open(file_json_placeholder, 'r')
    jsondata_open_place = file_response_placeholder.read()
    obj = json.loads(jsondata_open_place)
    assert str(obj['userId']) == "1"
    assert str(obj['id']) == "1"
    assert str(obj['title']) == "delectus aut autem"
    assert str(obj['completed']) == "False"


# Check request post with parameters
@pytest.mark.smoke
@pytest.mark.parametrize('user_id_in, user_id_out',
                         [(0, "0"),
                          (-1, "-1"),
                          (1, "1")])
@pytest.mark.parametrize('in_title, out_title',
                         [('title', 'title'),
                          ("", ""),
                          ("ay", "ay"),
                          (10, "10"),
                          (100, "100"),
                          (1000, "1000"),
                          ("$", "$")])
def test_jsonplaseholder_request_post(base_url, user_id_in, user_id_out, in_title, out_title):
    res = requests.post(
        base_url + "/posts",
        data={'title': in_title, 'body': 'bar', 'userId': user_id_in})
    res_json = res.json()
    assert res_json['title'] == out_title
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == user_id_out
