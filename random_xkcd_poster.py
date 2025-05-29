import random

from decouple import config
import requests
import telegram


def get_last_comics_num():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    xkcd_last_comics_response = response.json()
    return xkcd_last_comics_response.get('num')


def fetch_comics(num):
    url = f'https://xkcd.com/{num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    xkcd_response = response.json()

    image_link = xkcd_response.get('img')
    description = xkcd_response.get('alt')

    return image_link, description


def post_on_telegram(bot, chat_id, image_link, description):
    try:
        bot.send_photo(chat_id=chat_id, photo=image_link, caption=description)
    except telegram.error.TelegramError as e:
        print(f'Ошибка при публикации: {e}')
    return print('Комикс опубликован!')


def main():
    last_comics_num = get_last_comics_num()
    random_comics_num = random.randint(1, last_comics_num)

    image_link, description = fetch_comics(random_comics_num)

    tg_token = config('TG_TOKEN')
    chat_id = config('CHAT_ID')
    bot = telegram.Bot(token=tg_token)

    post_on_telegram(bot, chat_id, image_link, description)


if __name__ == '__main__':
    main()
