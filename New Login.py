import os
import time, os, fileinput, csv, json, random, subprocess, configparser
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagrapi.exceptions import BadPassword, TwoFactorRequired, ChallengeRequired, ChallengeUnknownStep, LoginRequired
from urllib3.exceptions import MaxRetryError
from datetime import datetime

# Create a Client Object
cl = Client()

try:
    exec(open("C:/blackaquapydroid/modules/config.py").read())
except FileNotFoundError:
    exec(open("/storage/emulated/0/blackaquapydroid/modules/config.py").read())


# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_datetime)



# Prompt user to enter a username
project = input("Please enter your username: ").strip()

# Prompt user to enter a password
password = input("Please enter your password (leave blank if none): ").strip()

# Save username to a file
with open(f"{database_directory}/projects/ReLogin.txt", "w") as f:
    f.write(project)
    print("Username saved to file.")

# Save password to a file if not empty
if password != "":
    with open(f"{database_directory}/passwords/{project}.txt", "w") as f:
        f.write(password)
        print("Password saved to file.")




# Path to the folder
folder_path = rf'{database_directory}/devices'

# Construct the file path
file_path = os.path.join(folder_path, f"{project}.json")

# Check if the file exists
if os.path.exists(file_path):
    print(f"Username already registered: {project}")
    time.sleep(1)
    exec(open(f"{python_directory}/modules/login.py").read())
    time.sleep(1)
else:
    print(f"Username not registered: {project}")
    print(f"Creating Device: {project}")
    time.sleep(1)
    exec(open(f"{python_directory}/modules/Create_Device.py").read())
    time.sleep(1)
    exec(open(f"{python_directory}/modules/login.py").read())
    time.sleep(1)

