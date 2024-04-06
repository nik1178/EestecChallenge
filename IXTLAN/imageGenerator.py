from openai import OpenAI
import os
import requests

API_KEY = open("./API_KEY.txt", "r").read()
client = OpenAI(
    api_key=API_KEY,
)

prompt_text = "An infographic showing two clusters of points in a 3D space, labeled 'X' and 'Y', with arrows indicating movement from cluster X to Y, representing the concept of rotating and moving a solid object from one position to another. The style should be clear, with a scientific and instructional look, suitable for a mathematical presentation."

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_text,
    size="1024x1024",
    quality="hd",
    n=1,
)

image_url = response.data[0].url
print(image_url)


with open('images/pic1.jpg', 'wb') as handle:
    response = requests.get(image_url, stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)