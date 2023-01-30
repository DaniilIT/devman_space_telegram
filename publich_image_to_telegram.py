import argparse
import os
import random

import telegram
from dotenv import dotenv_values


CHANNEL_ID = '@MyKosmos_DaniilIt'


def publich_image_to_telegram(image, token):
    if not image:
        image = random.choice(os.listdir('./images'))

    bot = telegram.Bot(token=token)
    bot.send_document(chat_id=CHANNEL_ID, document=open(f'./images/{image}', 'rb'))


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
    telegram_token = dotenv_values('.env')['TELEGRAM_TOKEN']

    publich_image_to_telegram(args.image, telegram_token)
