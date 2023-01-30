import argparse
import os
import random

import telegram
from dotenv import dotenv_values


def publich_image_to_telegram(image, channel_id, token):
    """Функция публикует фотографию в telegram канал
    """
    if not image:
        image = random.choice(os.listdir('./images'))

    bot = telegram.Bot(token=token)

    with open(f'./images/{image}', 'rb') as document:
        bot.send_document(chat_id=channel_id, document=document)


def create_parser():
    """Функция производит синтаксический анализ командной строки
    """
    parser = argparse.ArgumentParser(
        description='Программа публикует фотографию в канал телеграма.'
    )
    parser.add_argument(
        '--image',
        help='Изображение для публикации',
    )
    return parser


if __name__ == '__main__':
    args = create_parser().parse_args()
    telegram_channel_id = dotenv_values('.env')['CHANNEL_ID']
    telegram_token = dotenv_values('.env')['TELEGRAM_TOKEN']

    publich_image_to_telegram(args.image, telegram_channel_id, telegram_token)
