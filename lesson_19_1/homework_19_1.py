import requests
import random

def get_random_image(data):
    image = random.choice(data['collection']['items'])
    return image['href']

base_url = 'https://images-api.nasa.gov/search?q=mars&media_type=image'
response = requests.get(base_url)
data = response.json()
#print(get_random_image(data))

#x = random.choice(data['collection']['items'])
#print(x['href'])
#print(data['collection']['items'][0]['href'])
#for item in data['collection']['items']:
#    print('-'*10)
#    print(item['links'])

r = requests.get(get_random_image(data))
print(r.content)
with open('image.jpg', 'wb') as nasa_image:
    nasa_image.write(r.content)
