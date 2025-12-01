import requests
import random

def get_random_image_url(data : dict) -> str:
    image = random.choice(data['collection']['items'])
    get_request = requests.get(image['href'])
    return get_request.json()[0]

def download_image(response : requests.Response, name : str) -> None:
     with open(f'{name}.jpg', 'wb') as nasa_image:
        nasa_image.write(response.content)


base_url = 'https://images-api.nasa.gov/search?q=mars&media_type=image'
base_response = requests.get(base_url)
base_data = base_response.json()

image_1 = get_random_image_url(base_data)
image_2 = get_random_image_url(base_data)
image_3 = get_random_image_url(base_data)

image_response_1 = requests.get(image_1)
image_response_2 = requests.get(image_2)
image_response_3 = requests.get(image_3)

download_image(image_response_1, 'image_1')
download_image(image_response_2, 'image_2')
download_image(image_response_3, 'image_3')


