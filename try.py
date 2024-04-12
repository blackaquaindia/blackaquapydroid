import time, os, fileinput, csv, json, random, subprocess, configparser
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagrapi.exceptions import BadPassword, TwoFactorRequired, ChallengeRequired, ChallengeUnknownStep, LoginRequired
from urllib3.exceptions import MaxRetryError
from datetime import datetime

# Create a Client Object
cl = Client()

# Prompt user to enter a username
project = input("Please enter your username: ").strip()

try:
    exec(open("C:/blackaquapydroid/modules/config.py").read())
except FileNotFoundError:
    exec(open("/storage/emulated/0/blackaquapydroid/modules/config.py").read())

exec(open(f"{python_directory}/modules/create_device.py").read())
