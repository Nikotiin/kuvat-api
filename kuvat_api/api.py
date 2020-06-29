"""
Raw JSON API of kuvat.fi
"""
from requests import Session

class Api:
    """
    Api encapsulates HTTP client
    """
    def __init__(self, base_url):
        """
        :param base_url: URL of kuvat.fi site
        """
        self.base_url = base_url
        self.http_client = Session()

    def get_directories(self):
        """
        Get all directories

        :return: JSON object of directories
        """
        params = {"type": "getFolderTree"}
        data = {"folder": ""}
        response = self.http_client.post(self.base_url, params=params, data=data)
        return response.json()

    def get_files(self, folder):
        """
        Get all files from folder

        :param folder: kuvat.fi folder
        :return: JSON object of files
        """
        params = {"type": "getFileListJSON"}
        data = {"folder": folder}
        response = self.http_client.post(self.base_url, params=params, data=data)
        return response.json()

    def authenticate(self, id_, password):
        """
        Authenticate user

        :param id_: ID of the directory
        :param password: Password
        """
        params = {"q": "folderpassword", "id": id_, "folderpassword": password}
        self.http_client.get(self.base_url, params=params)

    def get_bytes(self, path):
        """
        Get file bytes

        :param path: Path of the file
        :return: Bytearray of file bytes
        """
        response = self.__get_file(path)
        return response.content

    def save_file(self, path, savepath):
        """
        Save file to disk

        :param path: Path of the kuvat.fi file
        :param savepath: Path, where file should be saved
        """
        response = self.__get_file(path)
        with open(savepath, 'wb') as file:
            for chunk in response.iter_content():
                file.write(chunk)

    def __get_file(self, path):
        params = {"img": "full"}
        response = self.http_client.get(self.base_url + path, params=params)
        return response
