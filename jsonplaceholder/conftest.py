import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com",
        help="This is base request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "path", "delete"],
        help="method to execute"
    )

    parser.addoption(
        "--encoding",
        default=["utf-8"],
        choices=["utf-8", "CP-1251"],
        help="encoding to execute"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))


file_json_placeholder = '/Users/apple/Documents/otus/lesson_api/test-api/jsonplaceholder/response.json'
