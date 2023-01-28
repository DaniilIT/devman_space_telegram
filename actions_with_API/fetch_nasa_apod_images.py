from sys import stderr

import requests
from dotenv import dotenv_values
from tqdm import tqdm

from actions_with_images import download_image, get_file_format


NASA_URL = "https://api.nasa.gov"
NASA_IMAGES_COUNT = 5


def fetch_nasa_apod_images(token, images_count):
    """Функция запрашивает через API NASA ссылки на изображения APOD и скачивает эти изображения.
    """
    try:
        payload = {
            'api_key': token,
            'count': images_count,
        }
        response = requests.get(f"{NASA_URL}/planetary/apod", params=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        stderr.write(f"Не удалось сделать запрос к API NASA APOD.\n")
    else:
        for image_number, image in tqdm(enumerate(response.json())):
            image_url = image['url']
            try:
                image_name = f"nasa_apod_{image_number}{get_file_format(image_url)}"
                download_image(image_url, image_name)
            except requests.exceptions.HTTPError:
                stderr.write(f"Не удалось скачать фотографию по адресу {image_url}.\n")


if __name__ == '__main__':
    nasa_token = dotenv_values(".env")['NASA_TOKEN']
    fetch_nasa_apod_images(nasa_token, NASA_IMAGES_COUNT)
