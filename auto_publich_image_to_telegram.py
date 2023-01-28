import argparse
import os
import random
import time

import telegram
from dotenv import dotenv_values


CHANNEL_ID = "@MyKosmos_DaniilIt"


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

    telegram_token = dotenv_values(".env")['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)

    while True:
        images = os.listdir("./images")
        random.shuffle(images)

        for image in images:
            bot.send_document(chat_id=CHANNEL_ID, document=open(f"./images/{image}", 'rb'))
            time.sleep(publish_delay)


if __name__ == '__main__':
    main()
