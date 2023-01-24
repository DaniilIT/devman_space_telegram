from pathlib import Path

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


def main():
    Path("./images").mkdir(exist_ok=True)

    try:
        response = requests.get(f'{SPACEX_URL}/v5/launches/{FLIGHT_ID}')
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


if __name__ == '__main__':
    main()
