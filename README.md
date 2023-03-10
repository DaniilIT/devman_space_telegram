# Космический Телеграм

Программа разделена на несколько скриптов: 
 
### - fetch_spacex_images
С помощью API SpaceX скачивает фотографии с одного запуска.

### - fetch_nasa_apod_images 
с помощью API NASA скачивает астрономические фотографии (APOD).

### - fetch_nasa_epic_images
с помощью API NASA скачивает фотографии Земли (EPIC).

Все фотографии скачиваются в папку `images/`.

### - publich_image_to_telegram
С помощью бота Telegram - BotFather, публикует одну фотографию в Telegram - канал
[@MyKosmos_DaniilIt](https://t.me/MyKosmos_DaniilIt), в котором бот является администратором.

### - auto_publich_image_to_telegram
Скрипт перемешивает в случайном порядке фотографии из папки `images/`
и раз в несколько часов публикует по одной в Telegram - канал.


## Как установить

Чтобы использовать API NASA, вам потребуется токен доступа, получите его [здесь](https://api.nasa.gov/).

Чтобы использовать BotFather, вам тоже потребуется токен доступа, получите его [здесь](https://telegram.me/BotFather).

Вставьте токены и id telegram - канала вида `@channel`, в файл .env, выполнив команды:

```
echo "NASA_TOKEN=<your nasa token>" >> .env
echo "TELEGRAM_TOKEN=<your botfather token>" >> .env
echo "CHANNEL_ID=<your channel id>" >> .env
```

Для этого проекта требуются следующие пакеты Python:

- python-dotenv >= 0.21.1
- requests >= 2.28.2
- python-telegram-bot == 13.0

Python3 должен быть уже установлен.
Затем используйте pip (или pip3, если есть конфликт с Python2) для установки этих зависимостей:

```Python
pip install -r requirements.txt
```


## Запуск

### - fetch_spacex_images

Для запуска скрипта наберите команду:
```Python
python actions_with_API/fetch_spacex_images.py
```

Вы также можете указать id конкретного запуска, например `--launch_id 5eb87d47ffd86e000604b38a`,
по умолчанию фотографии скачиваются с последнего запуска.

### - fetch_nasa_apod_images

Для запуска скрипта наберите команду:
```Python
python actions_with_API/fetch_nasa_apod_images.py
```

### - fetch_nasa_epic_images

Для запуска скрипта наберите команду:
```Python
python actions_with_API/fetch_nasa_epic_images.py
```

### - publich_image_to_telegram

Для запуска скрипта наберите команду:
```Python
python publich_image_to_telegram.py
```

Вы также можете указать фотографию для публикации, например `--image nasa_epic_1.png`,
по умолчанию публикуется случайная фотография.

### - auto_publich_image_to_telegram

Для запуска скрипта наберите команду:
```Python
python auto_publich_image_to_telegram.py
```

Вы также можете указать количество часов между публикациями, например `--publish_delay 12`,
по умолчанию 4 часа между публикациями.


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
