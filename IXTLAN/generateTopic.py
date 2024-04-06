from openai import OpenAI
import os
import io
import requests

conversation_messages = []

API_KEY = open("./API_KEY.txt", "r").read()

instruction = "You build latex code to make slides for a presentation. You are given the text about a topic, turn it into bullet points, and add images to the slides. Make sure that they are scaled properly. Pretend that the images exist in a local folder called \"./images\", and add them to the code normally. Try to add an image to every slide. Every presentation starts with an opening slide with a title, featuring the authors' names and affiliations. The following slides contain bullet points with the main ideas of the presentation. Make sure you include most of the topics and/or section. The final topic slide is a conclusion slide with a summary of the presentation. The slides should be visually appealing and easy to read. The text should be concise and to the point. The images should be relevant to the text and help illustrate the main ideas. The presentation should be engaging and informative. If possible, add one more slide with references, if those were given in the starting text. The presentation should be professional and well-organized. The true final two slides should be for questions and thank you. WRITE NOTHING BUT THE CODE, NO MATTER WHAT, ONLY GIVE THE CODE. The input text is:"


input_file = open("input_file.txt", "r", errors="ignore")
input_text = input_file.read()


client = OpenAI(
    api_key=API_KEY,
)

conversation_messages.append({"role": "user", "content": "Generate an aproximetly 200 word script about a program where AI creates a slide presentation and script for you."},)
response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=conversation_messages
)

print(response.choices[0].message.content)