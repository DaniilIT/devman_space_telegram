from dotenv import dotenv_values
import telegram


def main():
    telegram_token = dotenv_values(".env")['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)

    bot.send_message(text='Hi Everyone from bot!', chat_id="@MyKosmos_DaniilIt")


if __name__ == '__main__':
    main()
