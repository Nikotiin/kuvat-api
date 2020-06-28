from requests import Session

class Api:
    def __init__(self, base_url):
        self.base_url = base_url
        self.http_client = Session()

    def get_directories(self):
        params = {"type": "getFolderTree"}
        data = {"folder": ""}
        response = self.http_client.post(self.base_url, params=params, data=data)
        return response.json()

    def get_files(self, folder):
        params = {"type": "getFileListJSON"}
        data = {"folder": folder}
        response = self.http_client.post(self.base_url, params=params, data=data)
        return response.json()

    def authenticate(self, id_, password):
        params = {"q": "folderpassword", "id": id_, "folderpassword": password}
        self.http_client.get(self.base_url, params=params)

    def get_bytes(self, path):
        response = self.__get_file(path)
        return response.content

    def save_file(self, path, savepath):
        response = self.__get_file(path)
        with open(savepath, 'wb') as file:
            for chunk in response.iter_content():
                file.write(chunk)

    def __get_file(self, path):
        params = {"img": "full"}
        response = self.http_client.get(self.base_url + path, params=params)
        return response
