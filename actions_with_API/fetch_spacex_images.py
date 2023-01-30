import argparse
from sys import stderr

import requests

from actions_with_images import download_image


SPACEX_URL = 'https://api.spacexdata.com'


def fetch_spacex_images(launch_id):
    """Функция запрашивает через API SpaceX ссылки на изображения и скачивает эти изображения.
    """
    try:
        response = requests.get(f'{SPACEX_URL}/v5/launches/{launch_id}')
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        stderr.write(f'Не удалось сделать запрос к API SpaceX.\n')
    else:
        for image_number, image_url in enumerate(response.json()['links']['flickr']['original']):
            try:
                image_name = f'spacex_{image_number + 1}.jpg'
                download_image(image_url, image_name)
            except requests.exceptions.HTTPError:
                stderr.write(f'Не удалось скачать фотографию по адресу {image_url}.\n')


def create_parser():
    """Функция производит синтаксический анализ командной строки
    """
    parser = argparse.ArgumentParser(
        description='Программа скачивает фото с запуска SpaceX'
    )
    parser.add_argument(
        '--launch_id',
        help='id запуска',
        default='latest',
    )
    return parser


if __name__ == '__main__':
    args = create_parser().parse_args()
    fetch_spacex_images(args.launch_id)
