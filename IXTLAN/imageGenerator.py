from openai import OpenAI
import os
import requests

API_KEY = open("./API_KEY.txt", "r").read()
client = OpenAI(
    api_key=API_KEY,
)

prompt_text = "Very simple single line dumbell drawings, for website background, beige background. Very spaced apart, a lot of space, not a lot of objects."

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_text,
    size="1024x1024",
    quality="hd",
    n=1,
)

image_url = response.data[0].url
print(image_url)


with open('pic1.jpg', 'wb') as handle:
    response = requests.get(image_url, stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)