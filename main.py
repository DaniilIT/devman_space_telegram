import os
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests


SPACEX_URL = "https://api.spacexdata.com"
FLIGHT_ID = '5eb87d47ffd86e000604b38a'


def download_image(url, file_path):
    """Функция скачивает изображение и сохраняет его
    """
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        f.write(response.content)


def fetch_spacex_last_launch(flight_id):
    """Функция запрашивает через API SpaceX ссылки на изображения и скачивает эти изображения.
    """
    Path("./images").mkdir(exist_ok=True)

    try:
        response = requests.get(f'{SPACEX_URL}/v5/launches/{flight_id}')
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Что-то пошло не так")
    else:
        for image_number, image_url in enumerate(response.json()['links']['flickr']['original']):
            try:
                image_file_path = f"./images/spacex{image_number}.jpg"
                download_image(image_url, image_file_path)
            except requests.exceptions.HTTPError:
                print("Что-то пошло не так")

def get_file_format(url):
    """Функция возвращает формат файла по адресу.
    """
    file_path = unquote(urlparse(url).path)
    file_format = os.path.splitext(file_path)[-1]
    return file_format



def main():
    # fetch_spacex_last_launch(FLIGHT_ID)
    print(get_file_format("https://example.com/txt/hello%20world.txt?v=9#python"))


if __name__ == '__main__':
    main()
