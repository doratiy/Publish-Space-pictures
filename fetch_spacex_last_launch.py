import requests
import os


def get_spacex_urls(folder):
    number_image = 0
    method_url = "https://api.spacexdata.com/v5/launches"
    params = {
        "id": "5eb87d46ffd86e000604b388"
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    for response in reversed(response.json()):
        if response["links"]["flickr"]["original"]:
            for image in response["links"]["flickr"]["original"]:
                number_image += 1
                image = requests.get(image)
                with open(f"{folder}/image_spacex_{number_image}.jpg", 'wb') as file:
                    file.write(image.content)
            return response["links"]["flickr"]["original"]


if __name__ == "__main__":
    folder = 'images'
    if not os.path.exists(folder):
        os.makedirs(folder)
    links_spacex = get_spacex_urls(folder)
