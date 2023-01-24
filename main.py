from pathlib import Path

import requests


def download_image(url, file_path):
    """Функция скачивает изображение и сохраняет его
    """
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        f.write(response.content)


def main():
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    image_file_path = "./images/hubble.jpeg"

    Path("./images").mkdir(exist_ok=True)

    try:
        download_image(image_url, image_file_path)
    except requests.exceptions.HTTPError:
        print("Что-то пошло не так")


if __name__ == '__main__':
    main()
