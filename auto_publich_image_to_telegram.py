import argparse
import os
import random
import time

from publich_image_to_telegram import publich_image_to_telegram


def create_parser():
    """Функция производит синтаксический анализ командной строки
    """
    parser = argparse.ArgumentParser(
        description="Программа автоматически публикует фотографии в канал телеграма."
    )
    parser.add_argument(
        '--publish_delay',
        help="Задержка в часах между публикациями.",
        default=4,
        type=int,
    )
    return parser


def main():
    args = create_parser().parse_args()
    publish_delay = args.publish_delay * 3600

    while True:
        images = os.listdir("./images")
        random.shuffle(images)

        for image in images:
            publich_image_to_telegram(image)
            time.sleep(publish_delay)


if __name__ == '__main__':
    main()
