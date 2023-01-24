from pathlib import Path

import requests


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()

    with open("./images/hubble.jpeg", 'wb') as f:
        f.write(response.content)


def main():
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

    Path("./images").mkdir(exist_ok=True)

    try:
        download_image(image_url)
    except requests.exceptions.HTTPError:
        print("Что-то пошло не так")


if __name__ == '__main__':
    main()
