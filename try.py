import time
import os
import fileinput
import os
import csv
import json
import time
import random
import subprocess
import configparser
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagrapi.exceptions import BadPassword
from instagrapi.exceptions import TwoFactorRequired
from instagrapi.exceptions import ChallengeRequired
from instagrapi.exceptions import ChallengeUnknownStep
from instagrapi.exceptions import LoginRequired
from urllib3.exceptions import MaxRetryError
from datetime import datetime

# Create a Client Object
cl = Client()

# Prompt user to enter a username
project = input("Please enter your username: ").strip()

exec(open(f"config.py").read())
exec(open(f"{python_directory}/modules/create_device.py").read())
