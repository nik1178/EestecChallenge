from openai import OpenAI
import os
import io
import requests
import shutil


API_KEY = open("./API_KEY.txt", "r").read()
instruction = "You build latex code to make slides for a presentation. You are given the text about a topic, turn it into bullet points, and add images to the slides. Make sure that they are scaled properly. Pretend that the images exist in a local folder called \"./images\", and add them to the code normally. Try to add an image to every slide. Every presentation starts with an opening slide with a title, featuring the authors' names and affiliations. The following slides contain bullet points with the main ideas of the presentation. Make sure you include most of the topics and/or section. The final topic slide is a conclusion slide with a summary of the presentation. The slides should be visually appealing and easy to read. The text should be concise and to the point. The images should be relevant to the text and help illustrate the main ideas. The presentation should be engaging and informative. If possible, add one more slide with references, if those were given in the starting text. The presentation should be professional and well-organized. The true final two slides should be for questions and thank you. WRITE NOTHING BUT THE CODE, NO MATTER WHAT, ONLY GIVE THE CODE. The input text is:"

instructions_get_image_prompts = "Now list all the images in the folder /images that you used, and give me the prompts for each one. These prompts should be good for image generating AI models. Make sure that the prompts are super accurate and descriptive, so that even if someone doesn't know the context at all, they would still understand what you want. Also make sure to specify in what style the image should be created. And you'll get a raise if they are good. GIVE NOTHING BUT THE OUTPUT IN THE SPECIFIED FORMAT, DO NOT WRITE ANYTHING ELSE. The output should be in the following format: ImageName1: {prompt1} \\n ImageName2: {prompt2} \\n ..."

class PresentationGenerator:
    
    conversation_messages = []
    conversation_messages.append({"role": "system", "content": instruction},)
    
    presentation_folder = "presentation"
        
    client = OpenAI(
        api_key=API_KEY,
    )
    
    def __init__(self, input_text):
        self.input_text = input_text
    
    def generate_latex_code(self):
        conversation_messages.append({"role": "user", "content": input_text},)
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=conversation_messages
        )

        message_text = response.choices[0].message.content
        conversation_messages.append({"role": "assistant", "content": message_text})
        
        # Remove ``` from the start and end of the code`
        
        latex_path = os.path.join(presentation_folder, "presentation.tex")
        if os.path.exists(latex_path):
            os.remove(latex_path)

        code_file =  open(latex_path, "a", errors="ignore")
        code_file.write(message_text)
    
    def generate_image_prompts(self):
        conversation_messages.append({"role": "system", "content": instructions_get_image_prompts},)
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=conversation_messages
        )
        
        message_text = response.choices[0].message.content
        return message_text

    def generate_images(self, image_prompts):
        
    
    def generate_presentation(self):
        latex_code = generate_latex_code()
        write_to_file("presentation.tex", latex_code)
        image_prompts = generate_image_prompts()
        generate_images(image_prompts)

print(response.choices[0].message.content)
image_message = response.choices[0].message.content
buff = io.StringIO(image_message)

if os.path.exists("images"):
    shutil.rmtree("images")
os.makedirs("images")

for line in buff:
    if len(line) < 2:
        continue
    split = line.split(":")
    image_name = split[0]
    prompt = split[1].strip()
    if prompt[0] == '{':
        prompt = prompt[1:]
    if prompt[-1] == '}':
        prompt = prompt[:-1]
    
    
    print("Current prompt: " + prompt)
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="hd",
        n=1,
    )

    image_url = response.data[0].url
    print("Generated: " + image_url)


    with open('images/'+image_name, 'wb') as handle:
        response = requests.get(image_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
