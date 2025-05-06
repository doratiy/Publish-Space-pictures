import datetime
import requests
from dotenv import load_dotenv
import os


def get_epic_pictures(epic_urls, token, folder):
    number_image = 0
    method_url = "https://api.nasa.gov/EPIC/api/natural/"
    date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y/%m/%d")
    params = {
        "date": date,
        "api_key": token
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    num = 0
    for picture_num in range(5):
        picture = response.json()[picture_num]["image"]
        url_picture = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{picture}.png?api_key={token}"
        epic_urls.append(url_picture)
        number_image += 1
        image = requests.get(url_picture)
        with open(f"{folder}/image_epic_{number_image}.png", 'wb') as file:
            file.write(image.content)
    return epic_urls


if __name__ == "__main__":
    load_dotenv()
    folder = 'images'
    if not os.path.exists(folder):
        os.makedirs(folder)
    token = os.environ["NASA_TOKEN"]
    epic_urls = []
    epic_urls = get_epic_pictures(epic_urls, token, folder)
