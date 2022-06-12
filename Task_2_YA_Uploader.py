import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_path = os.path.normpath(file_path)

        HEADERS = {"Authorization" : f'OAuth {self.token}'}
        FILES = {"file" : open(file_path, 'rb')}

        response_url = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        params = {"path": file_path, "overwrite": True} ,
        headers = HEADERS)
        url = response_url.json().get('href')

        response_upload = requests.put(url, files = FILES, headers = {})
        return print(response_upload.status_code)


if __name__ == '__main__':
    path_to_file = input("Enter path to uploaded file: ")
    token = input("Enetr your token: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)