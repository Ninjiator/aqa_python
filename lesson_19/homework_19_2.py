import requests

base_url = "http://127.0.0.1:8080"

post_path = '/upload'

with open("images.jpeg", "rb") as image_file:
    image_data = image_file.read()
    file = {"image" : ('images.jpeg', image_data, "image/jpeg")}
response_post = requests.post(base_url + post_path, files = file)
print(f'Post results: Status is {response_post.status_code},\nText: {response_post.text}')

get_path = f'/image/{image_file.name}'
header_text = {'Content-Type' : 'text'}
response_get = requests.get(base_url + get_path, headers = header_text)
print(f'Get results: Status is {response_get.status_code},\nText: {response_get.text}')

delete_path = f"/delete/{image_file.name}"
delete_response = requests.delete(base_url + delete_path)
print(f'Delete results: Status is {delete_response.status_code},\nText: {delete_response.text}')