import datetime
from sys import stderr

from dotenv import dotenv_values
import requests

from actions_with_images import download_image


NASA_URL = 'https://api.nasa.gov'


def fetch_nasa_epic_images(token):
    """Функция запрашивает через API NASA ссылки на изображения EPIC и скачивает эти изображения.
    """
    try:
        payload = {
            'api_key': token,
        }
        response = requests.get(f'{NASA_URL}/EPIC/api/natural', params=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        stderr.write(f'Не удалось сделать запрос к API NASA EPIC.\n')
    else:
        for image_number, image in enumerate(response.json()):
            image_name = image['image']
            image_date = datetime.datetime.fromisoformat(image['date'])
            image_url = f'{NASA_URL}/EPIC/archive/natural/{image_date.strftime("%Y/%m/%d")}/png/{image_name}.png'
            try:
                image_name = f'nasa_epic_{image_number + 1}.png'
                download_image(image_url, image_name, token=token)
            except requests.exceptions.HTTPError:
                stderr.write(f'Не удалось скачать фотографию по адресу {image_url}.\n')


if __name__ == '__main__':
    nasa_token = dotenv_values('.env')['NASA_TOKEN']
    fetch_nasa_epic_images(nasa_token)
