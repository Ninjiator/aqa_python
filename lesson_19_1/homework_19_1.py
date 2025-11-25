import requests
import random

def get_random_image(data):
    image = random.choice(data['collection']['items'])
    return image['href']

base_url = 'https://images-api.nasa.gov/search?q=mars&media_type=image'
response = requests.get(base_url)
data = response.json()

r = requests.get(get_random_image(data))
print(r.json()[0])
image_url = str(r.json()[0])
response_get = requests.get(image_url)



with open('image.jpg', 'wb') as nasa_image:
    nasa_image.write(response_get.content)
