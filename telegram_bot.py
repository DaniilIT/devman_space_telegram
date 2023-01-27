from dotenv import dotenv_values
import telegram


CHANNEL_ID = "@MyKosmos_DaniilIt"


def main():
    telegram_token = dotenv_values(".env")['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)

    # bot.send_message(text='Hi Everyone from bot!', chat_id=CHANNEL_ID)
    bot.send_document(chat_id=CHANNEL_ID, document=open('./images/spacex_0.jpg', 'rb'))


if __name__ == '__main__':
    main()
