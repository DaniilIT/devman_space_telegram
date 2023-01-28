import argparse
import os
import random

import telegram
from dotenv import dotenv_values


CHANNEL_ID = "@MyKosmos_DaniilIt"


def create_parser():
    """Функция производит синтаксический анализ командной строки
    """
    parser = argparse.ArgumentParser(
        description="Программа публикует фотографию в канал телеграма."
    )
    parser.add_argument(
        '--image',
        help="Изображение для публикации",
    )
    return parser


def main():
    telegram_token = dotenv_values(".env")['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)

    args = create_parser().parse_args()
    if not args.image:
        args.image = random.choice(os.listdir("./images"))

    bot.send_document(chat_id=CHANNEL_ID, document=open(f"./images/{args.image}", 'rb'))


if __name__ == '__main__':
    main()
