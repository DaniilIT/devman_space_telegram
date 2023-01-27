import os
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests


def download_image(url, image_name, token=None):
    """Функция скачивает изображение и сохраняет его в файл
    """
    payload = {'api_key': token} if token else {}

    response = requests.get(url, params=payload)
    response.raise_for_status()

    image_path = "./images"
    Path(image_path).mkdir(exist_ok=True)

    with open(f"{image_path}/{image_name}", 'wb') as f:
        f.write(response.content)


def get_file_format(url):
    """Функция возвращает формат файла по адресу
    """
    file_path = unquote(urlparse(url).path)
    file_format = os.path.splitext(file_path)[-1]
    return file_format
