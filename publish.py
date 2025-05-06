from tg_bot import tg_bot
from dotenv import load_dotenv
from tg_bot import get_all_links
import os
import random
import argparse


def publish(urls, delay, chat_id, token):
    random.shuffle(urls)
    tg_bot(urls, delay, chat_id, token)


if __name__ == "__main__":
    folder = "images"
    urls = []
    load_dotenv()
    parser = argparse.ArgumentParser(
        description = 'Описание что делает программа'
    )
    parser.add_argument('-delay',
    '--delay',
    help = 'Ваша ссылка',
    default = 14400,
    type = int)
    args = parser.parse_args()
    delay = args.delay
    token = os.environ["TG_BOT_TOKEN"]
    token_nasa = os.environ["NASA_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    epic_urls = []
    urls = get_all_links(urls, token_nasa, folder)
    publish(urls, delay, chat_id, token)
