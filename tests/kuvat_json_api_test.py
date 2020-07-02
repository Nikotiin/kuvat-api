import pytest
import requests
from kuvat_api import Api, ConnectionException

@pytest.fixture
def mock_requests(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.exceptions.RequestException

    monkeypatch.setattr(requests.Session, "get", mock_get)

def test_get_directories_exception(mock_requests):
    api = Api("")

    with pytest.raises(ConnectionException):
        api.get_directories()

def test_get_files_exception(mock_requests):
    api = Api("")

    with pytest.raises(ConnectionException):
        api.get_files("")

def test_get_bytes_exception(mock_requests):
    api = Api("")

    with pytest.raises(ConnectionException):
        api.get_bytes("")

def test_authenticate_exception(mock_requests):
    api = Api("")

    with pytest.raises(ConnectionException):
        api.authenticate("", "")
