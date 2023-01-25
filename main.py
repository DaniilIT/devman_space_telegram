import os
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
from dotenv import dotenv_values


SPACEX_URL = "https://api.spacexdata.com"
SPACEX_LAUNCH_ID = "5eb87d47ffd86e000604b38a"
NASA_URL = "https://api.nasa.gov"
NASA_IMAGES_NUM = 5


def download_image(url, file_path):
    """Функция скачивает изображение и сохраняет его
    """
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        f.write(response.content)


def fetch_spacex_last_launch(launch_id):
    """Функция запрашивает через API SpaceX ссылки на изображения и скачивает эти изображения.
    """
    try:
        response = requests.get(f"{SPACEX_URL}/v5/launches/{launch_id}")
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Что-то пошло не так")
    else:
        for image_number, image_url in enumerate(response.json()['links']['flickr']['original']):
            try:
                image_file_path = f"./images/spacex_{image_number}.jpg"
                download_image(image_url, image_file_path)
            except requests.exceptions.HTTPError:
                print("Что-то пошло не так")


def get_file_format(url):
    """Функция возвращает формат файла по адресу.
    """
    file_path = unquote(urlparse(url).path)
    file_format = os.path.splitext(file_path)[-1]
    return file_format


def fetch_nasa_apod(token, images_num):
    """Функция запрашивает через API NASA ссылки на изображения и скачивает эти изображения.
    """
    try:
        payload = {
            'api_key': token,
            'count': images_num,
        }
        response = requests.get(f"{NASA_URL}/planetary/apod", params=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Что-то пошло не так")
    else:
        for image_number, image in enumerate(response.json()):
            image_url = image['url']
            try:
                image_file_path = f"./images/nasa_apod_{image_number}{get_file_format(image_url)}"
                download_image(image_url, image_file_path)
            except requests.exceptions.HTTPError:
                print("Что-то пошло не так")


def main():
    nasa_token = dotenv_values(".env")['NASA_TOKEN']
    Path("./images").mkdir(exist_ok=True)

    fetch_spacex_last_launch(SPACEX_LAUNCH_ID)
    fetch_nasa(nasa_token, NASA_IMAGES_NUM)


if __name__ == '__main__':
    main()
