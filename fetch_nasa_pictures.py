import requests
from dotenv import load_dotenv
import os


def get_nasa_pictures(token_nasa,folder):
    number_image = 0
    links_nasa = []
    method_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 30,
        "api_key": token_nasa
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    for response in (response.json()):
        if response["media_type"] == "image":
            links_nasa.append(response["url"])
            number_image += 1
            ext = os.path.splitext(response["url"])[1]
            image = requests.get(response["url"])
            with open(f"{folder}/image_apod_{number_image}{ext}", 'wb') as file:
                file.write(image.content)
    return links_nasa


if __name__ == "__main__":
    folder = 'images'
    if not os.path.exists(folder):
        os.makedirs(folder)
    load_dotenv()
    token_nasa = os.environ["NASA_TOKEN"]
    links_nasa = get_nasa_pictures(token_nasa, folder)
