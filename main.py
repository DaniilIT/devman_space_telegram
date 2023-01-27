import argparse

from dotenv import dotenv_values

from actions_with_API_space_images.fetch_spacex_images import *
from actions_with_API_space_images.fetch_nasa_apod_images import *
from actions_with_API_space_images.fetch_nasa_epic_images import *


NASA_IMAGES_COUNT = 5


def create_parser():
    """Функция производит синтаксический анализ командной строки
    """
    parser = argparse.ArgumentParser(
        description="Программа скачивает фото с запуска SpaceX"
    )
    parser.add_argument(
        '--launch_id',
        help="id запуска",
        default='latest',
    )
    return parser


def main():
    args = create_parser().parse_args()
    nasa_token = dotenv_values(".env")['NASA_TOKEN']

    fetch_spacex_images(args.launch_id)
    fetch_nasa_apod_images(nasa_token, NASA_IMAGES_COUNT)
    fetch_nasa_epic_images(nasa_token)


if __name__ == '__main__':
    main()
