import requests
import os

current = os.getcwd()
folder = 'folder for task 2'
file = 'text for task 2.txt'
full_path = os.path.join(current, folder, file)


TOKEN = ""


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # def get_files_list(self):
    #     files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    #     headers = self.get_headers()
    #     response = requests.get(files_url,headers=headers)
    #     return response.json()


    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        return href


    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path)
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print(f'Файл {file} успешно загружен')


if __name__ == "__main__":
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(os.path.join("netology/", file), full_path)





    # pprint(ya.get_files_list())
    # data = ya.get_files_list()
    # for item in data['items']:
    #     print(item['media_type'])