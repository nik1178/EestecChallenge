# SlAIdi

An AI powered program for simple generation of presentation slides and scripts, with simple customization.

### Use
When running the program (`slaidi.py`), you will be greeted with a simple window, asking whether you have only a topic, a whole script, or maybe even a full article made on a topic.
When you select which you have, enter your corresponding text, and everything will be generated shortly (takes a few minutes due to API requests), when a folder will open with your files.
You can also select a custom background image, if you don't want an automatically generated one.

### Customization
If you find any small issue, you can easily fix it inside the LaTeX file, and if you don't like any of the images, you can easily replace them within the "images" folder.

### Implementation
Works based on ChatGPT 4.0 and Dall-E 3.
Outputs a text file with the script, a PDF file with the presentation slides, and a .tex (LaTeX) file with the code for generating the slides.

### Required dependencies
* flet
* openai
* pillow