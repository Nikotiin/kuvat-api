from requests import Session
from .api import Api

class Client:
    def __init__(self, base_url):
        self.base_url = base_url
        self.api = Api(base_url)

    def get_directories(self):
        directories = []
        response = self.api.get_directories()
        for name, data in response.items():
            authenticated = False
            if data["auth"] is not None:
                authenticated = True
            directories.append(Directory(self.api, data["id"], name, authenticated, data["k"]))
        return directories

class Directory:
    def __init__(self, api, id_, name, authenticated, description=""):
        self.api = api
        self.id_ = id_
        self.name = name
        self.authenticated = authenticated
        self.description = description

    def __repr__(self):
        return self.name

    def get_files(self):
        files = []
        response = self.api.get_files(self.name)
        for file in response:
            files.append(File(self.api, file["filename"], file["filepath"], file["kuvaus"]))
        return files

    def authenticate(self, password):
        self.api.authenticate(self.id_, password)
        self.authenticated = True

class File:
    def __init__(self, api, name, path, description=""):
        self.api = api
        self.name = name
        self.path = path
        self.descripion = description

    def __repr__(self):
        return self.name

    def get_bytes(self):
        return self.api.get_file(self.path)

    def save(self, path):
        return self.api.save_file(self.path, path)
