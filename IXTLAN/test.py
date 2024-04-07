from openai import OpenAI
import os
import io
import requests
import shutil
from PIL import Image, ImageStat, ImageEnhance

def darken_background():
        
    final_background_path = os.path.join("background.png")
    
    img = Image.open(final_background_path).convert("RGB")
    
    img_enhancer = ImageEnhance.Brightness(img)
    enhanced_output = img_enhancer.enhance(0.4)
    enhanced_output.save("darkened_background.png")
    
darken_background()