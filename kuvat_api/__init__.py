"""
Kuvat.fi API
"""
from .api import Api
from .exceptions import *

class Client:
    """
    Client encapsulates Api object
    """
    def __init__(self, base_url):
        """
        :param base_url: URL of kuvat.fi site
        """
        self.base_url = base_url
        self.api = Api(base_url)

    def get_directories(self):
        """
        Get all image directories

        :return: List of Directory objects
        """
        directories = []
        response = self.api.get_directories()
        for name, data in response.items():
            # When API returns "auth: null", user is not authenticated
            authenticated = False
            if data["auth"] is not None:
                authenticated = True
            directories.append(Directory(self.api, data["id"], name, authenticated, data["k"]))
        return directories

class Directory:
    """
    Directory represents kuvat.fi directory
    """
    def __init__(self, api, id_, name, authenticated, description=""):
        """
        :param api: Instance of Api class
        :param id_: ID of the directory
        :param name: Name of the directory
        :param authenticated: Is user authenticated to open the directory
        :param description: Description of the directory
        """
        self.api = api
        self.id_ = id_
        self.name = name
        self.authenticated = authenticated
        self.description = description

    def __repr__(self):
        return self.name

    def get_files(self):
        """
        Get all images from the directory

        :return: List of Image objects
        """
        files = []
        response = self.api.get_files(self.name)

        if isinstance(response, dict) and response.get("error"):
            raise AuthenticationException("Not authenticated")

        for file in response:
            files.append(File(self.api, file["filename"], file["filepath"], file["kuvaus"]))
        return files

    def authenticate(self, password):
        """
        Authenticate user

        :param password: Password of the directory
        :return: True if authentication was successfull
        """
        response = self.api.authenticate(self.id_, password)

        if response["status"] == 1:
            self.authenticated = True
        else:
            self.authenticated = False

        return self.authenticated

class File:
    """
    File represents kuvat.fi image
    """
    def __init__(self, api, name, path, description=""):
        """
        :param api: Instance of Api class
        :param name: Name of the file
        :param path: Path of the file
        :param description: Description of the file
        """
        self.api = api
        self.name = name
        self.path = path
        self.descripion = description

    def __repr__(self):
        return self.name

    def get_bytes(self):
        """
        Get file bytes

        :return: Bytearray of file
        """
        return self.api.get_file(self.path)

    def save(self, path):
        """
        Save the file to disk

        :param path: Filepath, where file should be saved
        """
        self.api.save_file(self.path, path)
