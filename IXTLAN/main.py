from openai import OpenAI
import os
import io
import requests
import shutil
from PIL import Image, ImageStat, ImageEnhance
import random
import time


API_KEY = open("./API_KEY.txt", "r").read()
instructions_get_image_prompts = "Now list all the images in the folder /images that you used, except for, and give me the prompts for each one. These prompts should be good for image generating AI models. Make sure that the prompts are super accurate and descriptive, so that even if someone doesn't know the context at all, they would still understand what you want. Also make sure to specify in what style the image should be created. Also generated a \"background.png\" image. And you'll get a raise if they are good. GIVE NOTHING BUT THE OUTPUT IN THE SPECIFIED FORMAT, DO NOT WRITE ANYTHING ELSE. The output should be in the following format: ImageName1: {prompt1} \\nImageName2: {prompt2} \\n..."

IMAGE_FOLDER_NAME = "images"
LATEX_FILE_NAME = "presentation.tex"

WHITE_FOREGROUND_SETTINGS = "\setbeamercolor{frametitle}{fg=white}\n\setbeamercolor{title}{fg=white}\n\setbeamercolor{author}{fg=white}\n\setbeamercolor{date}{fg=white}\n\setbeamercolor{normal text}{fg=white}"

class PresentationGenerator:
    
    instruction = "You build latex code to make slides for a presentation. You are given the text about a topic, turn it into bullet points, and add images to every slide. Make sure that their width is set to 0.5 and MAKE SURE THE IMAGES ARE CENTERED. Pretend that the images exist in a local folder called \"./images\", and add them to the code normally. Try to add an image to every slide. Every slide has the same background from the image \"background.png\". Every presentation starts with an opening slide with a title, featuring the authors' names and affiliations. The following slides contain bullet points with the main ideas of the presentation. Make sure you include most of the topics and/or section. The final topic slide is a conclusion slide with a summary of the presentation. The slides should be visually appealing and easy to read. The text should be concise and to the point. The images should be relevant to the text and help illustrate the main ideas. The presentation should be engaging and informative. If possible, add one more slide with references, if those were given in the starting text. The presentation should be professional and well-organized. The true final two slides should be for questions and thank you and they both need images. WRITE NOTHING BUT THE CODE, NO MATTER WHAT, ONLY GIVE THE CODE. The input text is:"
    
    topic_script_instruction = "Generate an aproximetly 200 word slide presentation script about:"
    file_script_instruction = "Generate an aproximetly 200 word slide presentation script from the presentation code you made."
    
    conversation_messages = []
    conversation_messages.append({"role": "system", "content": instruction},)
    
    presentation_folder = "presentation"
    
    # do_white_text = False
        
    client = OpenAI(
        api_key=API_KEY,
    )
    
    def __init__(self, input_text, input_type, background_image_path=None):
        self.input_text = input_text
        self.input_type = input_type
        self.background_image_path = background_image_path
    
    # def brightness(self, file_path):
        
    #     shutil.copy(file_path, "temp.png")
        
    #     im = Image.open("temp.png").convert('L')
    #     stat = ImageStat.Stat(im)
        
    #     os.remove("temp.png")
        
    #     return stat.mean[0]
    
    # def set_font_color(self):
    #     print("Selecting font color")
    #     if self.background_image_path is None:
    #         return
        
    #     background_image_path_final = os.path.join(self.presentation_folder, IMAGE_FOLDER_NAME, "background.png")
    #     brightness = self.brightness(background_image_path_final)
    #     print("Brightness: " + str(brightness))
        
    #     if brightness < 127:
    #         print("The background is dark, so the font color should be white.")
    #         self.do_white_text = True
    
    def generate_script_from_topic(self):
        print("Generating script from topic")
        
        input_message = [{"role": "system", "content": self.topic_script_instruction}]
        input_message.append({"role": "user", "content": self.input_text})
        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=input_message
        )
        
        print("Script generated from topic")
        
        return response.choices[0].message.content
        
    
    def generate_latex_code(self):
        print("Generating latex code")
        self.conversation_messages.append({"role": "user", "content": self.input_text},)
        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=self.conversation_messages
        )

        message_text = response.choices[0].message.content
        self.conversation_messages.append({"role": "assistant", "content": message_text})
        
        # Remove ``` from the start and end of the code`
        if message_text[0:3] == "```":
            if message_text[0:8] == "```latex":
                message_text = message_text[8:]
            else:
                message_text = message_text[3:]
                
        message_text = message_text.replace('`', "")
        
        latex_path = os.path.join(self.presentation_folder, LATEX_FILE_NAME)
        if os.path.exists(latex_path):
            os.remove(latex_path)

        code_file =  open(latex_path, "a", errors="ignore")
        code_file.write(message_text)
        code_file.close()
        
        print("Latex code generated")
        
    def generate_image_prompts(self):
        print("Generating image prompts")
        self.conversation_messages.append({"role": "system", "content": instructions_get_image_prompts},)
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=self.conversation_messages
        )
        
        message_text = response.choices[0].message.content
        return message_text

    def generate_images(self, image_prompts):
        print("Generating images")
        folder_path = os.path.join(self.presentation_folder, "images")
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)
        
        buff = io.StringIO(image_prompts)

        

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
            
            print("Generating image: " + image_name)
            print("Current prompt: " + prompt)
            
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            print("Generated: " + image_url)


            with open(os.path.join(folder_path,image_name), 'wb') as handle:
                response = requests.get(image_url, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
    
    def darken_background(self, path):
        
        final_background_path = os.path.join(path)
        
        img = Image.open(final_background_path).convert("RGB")
        
        img_enhancer = ImageEnhance.Brightness(img)
        enhanced_image = img_enhancer.enhance(0.4)
        
        os.remove(path)
        
        enhanced_image.save(path)
    
    def change_background(self):
        print("Changing background")
        if self.background_image_path is None:
            print("No background image provided")
            return
        destination_path = os.path.join(self.presentation_folder, IMAGE_FOLDER_NAME, "background.png")
        
        if os.path.exists(destination_path):
            os.remove(destination_path)
            
        
        shutil.copy(self.background_image_path, destination_path)
        
        print("Background changed")
    
        
    def change_foreground(self):
        print("Changing foreground")
        # if not self.do_white_text:
        #     print("No need to change foreground")
        #     return
        
        latex_path = os.path.join(self.presentation_folder, LATEX_FILE_NAME)
        filedata = ""
        with open(latex_path, 'r') as file:
            filedata = file.read()
        
        os.remove(latex_path)
        
        filedata = filedata.split("\n")
        filedata.insert(2, WHITE_FOREGROUND_SETTINGS)
        
        with open(latex_path, "w") as file:
            file.write("\n".join(filedata))
            
        print("Foreground changed")
        
    def generate_script_from_file(self):
        print("Generating script from file")
        
        self.conversation_messages.append({"role": "system", "content": self.file_script_instruction},)
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=self.conversation_messages
        )
        
        message_text = response.choices[0].message.content
        return message_text
        
        
        print("Script generated from file")
        
    def save_script(self, script):
        print("Saving script")
        script_path = os.path.join(self.presentation_folder, "script.txt")
        
        script_file = open(script_path, "a", errors="ignore")
        script_file.write(script)
        script_file.close()
        
        print("Script saved")
                    
                    
    def compile_latex(self):
        try:
            path = os.path.join(os.getcwd(), self.presentation_folder)
            print("Current working directory: {0}".format(os.getcwd()))
            os.chdir(path)
            os.system("pdflatex " + LATEX_FILE_NAME)
            
            return
        except Exception as e:
            print(e)
            return
    
    def generate_presentation(self):
        
        if os.path.exists(self.presentation_folder):
            shutil.rmtree(self.presentation_folder)
        os.makedirs(self.presentation_folder)
        
        if self.input_type == 0:
            self.input_text = self.generate_script_from_topic()
            self.save_script(self.input_text)
        
        self.generate_latex_code()
        
        
        image_prompts = self.generate_image_prompts()
        print("Image prompts: " + image_prompts)
        self.generate_images(image_prompts)
        self.change_background()
        # self.set_font_color()
        self.darken_background(os.path.join(self.presentation_folder, IMAGE_FOLDER_NAME, "background.png"))
        self.change_foreground()
        
        if self.input_type == 2:
            script = self.generate_script_from_file()
            self.save_script(script)
            
        self.compile_latex()
        
        print("Finished generating presentation")