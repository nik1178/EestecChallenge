from openai import OpenAI
import os
import io
import requests
import shutil
from PIL import Image, ImageStat, ImageEnhance
import subprocess

def compile_latex():
    try:
        path = os.path.join(os.getcwd(), "presentation89803")
        print("Current working directory: {0}".format(os.getcwd()))
        os.chdir(path)
        os.system("pdflatex presentation.tex")
        
        return
    except Exception as e:
        print(e)
        return "timeout"

compile_latex()