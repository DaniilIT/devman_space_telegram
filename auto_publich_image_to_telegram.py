import argparse
import os
import random
import time

from dotenv import dotenv_values

from publich_image_to_telegram import publich_image_to_telegram


def auto_publich_image_to_telegram(publish_delay, channel_id, token):
    """Функция периодически публикует по одной случайной фотографии в telegram канал
    """
    publish_delay *= 3600

    while True:
        images = os.listdir('./images')
        random.shuffle(images)

        for image in images:
            publich_image_to_telegram(image, channel_id, token)
            time.sleep(publish_delay)


def create_parser():
    """Функция производит синтаксический анализ командной строки
    """
    parser = argparse.ArgumentParser(
        description='Программа автоматически публикует фотографии в канал телеграма.'
    )
    parser.add_argument(
        '--publish_delay',
        help='Задержка в часах между публикациями.',
        default=4,
        type=int,
    )
    return parser


if __name__ == '__main__':
    args = create_parser().parse_args()
    telegram_channel_id = dotenv_values('.env')['CHANNEL_ID']
    telegram_token = dotenv_values('.env')['TELEGRAM_TOKEN']

    auto_publich_image_to_telegram(args.publish_delay, telegram_channel_id, telegram_token)
