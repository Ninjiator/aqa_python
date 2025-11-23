import requests

base_url = 'http://127.0.0.1:8000'
url_post = base_url + '/upload'
with open("image.jpg", "rb") as file:
    files = {"image": ("image.jpg", file, "image/jpeg")}

    response_post = requests.post(url_post, files=files)
    data = response_post.json()

print(data)

url_get = 'http://127.0.0.1:8080/image/image.jpg'
response_get = requests.get(url_get)




