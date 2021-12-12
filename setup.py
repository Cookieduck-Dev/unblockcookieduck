#setup for heroku deployment
import os 
os.system("pip install setuptools")
os.system("pip install git+https://github.com/Cookieduck-Dev/unblockcookieduck")
os.system("python main.py")
