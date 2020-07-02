import pytest
from kuvat_api import Client, Directory, Api
from kuvat_api.exceptions import AuthenticationException

@pytest.fixture
def mock_get_directories_api(monkeypatch):
    response = {
        "test1": {
            "id": "1",
            "auth": True,
            "k": "desc1"
        },
        "test2": {
            "id": "2",
            "auth": None,
            "k": "desc2"
        }
    }

    def mock_get(*args, **kwargs):
        return response

    monkeypatch.setattr(Api, "get_directories", mock_get)

def test_get_directories(mock_get_directories_api):
    client = Client("")
    directories = client.get_directories()

    assert len(directories) == 2

def test_get_directories_id(mock_get_directories_api):
    client = Client("")
    directories = client.get_directories()

    assert directories[0].id_ == "1"
    assert directories[1].id_ == "2"

def test_get_directories_auth(mock_get_directories_api):
    client = Client("")
    directories = client.get_directories()

    assert directories[0].authenticated
    assert not directories[1].authenticated

def test_get_directories_description(mock_get_directories_api):
    client = Client("")
    directories = client.get_directories()

    assert directories[0].description == "desc1"
    assert directories[1].description == "desc2"

@pytest.fixture
def mock_get_files_api(monkeypatch):
    response = [
        {
            "filename": "file1",
            "filepath": "/file1",
            "kuvaus": "desc1"
        },
        {
            "filename": "file2",
            "filepath": "/file2",
            "kuvaus": "desc2"
        }
    ]

    def mock_get_files(*args, **kwargs):
        return response

    monkeypatch.setattr(Api, "get_files", mock_get_files)

@pytest.fixture
def mock_get_files_api_empty(monkeypatch):
    def mock_get_files(*args, **kwargs):
        return []

    monkeypatch.setattr(Api, "get_files", mock_get_files)

@pytest.fixture
def mock_get_files_api_error(monkeypatch):
    def mock_get_files(*args, **kwargs):
        return {"error": True}

    monkeypatch.setattr(Api, "get_files", mock_get_files)

def test_get_files(mock_get_files_api):
    directory = Directory(Api(""), "", "", True)
    files = directory.get_files()

    assert len(files) == 2

def test_get_files_name(mock_get_files_api):
    directory = Directory(Api(""), "", "", True)
    files = directory.get_files()

    assert files[0].name == "file1"
    assert files[1].name == "file2"

def test_get_files_path(mock_get_files_api):
    directory = Directory(Api(""), "", "", True)
    files = directory.get_files()

    assert files[0].path == "/file1"
    assert files[1].path == "/file2"

def test_get_files_description(mock_get_files_api):
    directory = Directory(Api(""), "", "", True)
    files = directory.get_files()

    assert files[0].descripion == "desc1"
    assert files[1].descripion == "desc2"

def test_get_files_empty(mock_get_files_api_empty):
    directory = Directory(Api(""), "", "", True)
    files = directory.get_files()

    assert len(files) == 0

def test_get_files_error(mock_get_files_api_error):
    directory = Directory(Api(""), "", "", True)

    with pytest.raises(AuthenticationException):
        directory.get_files()

@pytest.fixture
def mock_authenticate_api(monkeypatch):
    def mock_authenticate(_, id_, *args, **kwargs):
        status = 0
        if id_ == "1":
            status = 1
        return {"status": status}

    monkeypatch.setattr(Api, "authenticate", mock_authenticate)

@pytest.fixture
def mock_authenticate_api_error(monkeypatch):
    def mock_authenticate(id_, *args, **kwargs):
        return {"status": 0}

    monkeypatch.setattr(Api, "authenticate", mock_authenticate)

def test_authenticate(mock_authenticate_api):
    directory = Directory(Api(""), "1", "", True)
    response = directory.authenticate("")

    assert response
    assert directory.authenticated

def test_authenticate_failed(mock_authenticate_api_error):
    directory = Directory(Api(""), "", "", True)
    response = directory.authenticate("")

    assert not response
    assert not directory.authenticated
