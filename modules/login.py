import json
import imaplib
import email
import re
import time
from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice
from instagrapi.exceptions import BadPassword, TwoFactorRequired, ChallengeRequired, ChallengeUnknownStep, UnknownError


def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.SMS:
        return get_code_from_sms(username)
    elif choice == ChallengeChoice.EMAIL:
        return get_code_from_email(username)
    return False


def get_code_from_email(username):
    # Time Delay for OTP to Arrive
    time.sleep(15)
    
    # Login to your email account
    print("Logging into Email OTP Server: BlackAquaIndia")
    mail = imaplib.IMAP4_SSL('us2.imap.mailhostbox.com')
    mail.login('otp@blackaqua.in', 'T!E@VRR0')
    
    # Select the inbox
    print("Checking Inbox")
    mail.select('inbox')
    
    # Search for the email containing the OTP
    print("Getting Latest Instagram Email")
    result, data = mail.search(None, 'FROM "security@mail.instagram.com" SUBJECT "" BODY ""')
    mail_ids = data[0].decode('utf-8').split()
    
    # Get the most recent email with the OTP
    latest_email_id = mail_ids[-1]
    result, data = mail.fetch(latest_email_id, '(RFC822)')
    
    # Parse the email to get the OTP
    print("Searching for Latest OTP")
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    code = re.search(r'\d{6}', email_message.get_payload()).group()
    
    # Logout from your email account
    mail.logout()
    
    return code


try:
    # Remove_Authorization_Data
    exec(open(f"{python_directory}/modules/remove_authorization_data.py").read())
    
    # Load device settings from a file
    exec(open(f"{python_directory}/modules/load_device_settings.py").read())
    
    # Load Password from File
    with open(f'{database_directory}/passwords/{project}.txt', 'r') as file:
        password = file.read().strip()
    
    # Login Instagram
    print(f"[Trying To Login Account: {project}]")
    cl.challenge_code_handler = challenge_code_handler
    cl.login(username=project, password=password)
    
    # Save device settings to a file
    cl.dump_settings(f'{database_directory}/devices/{project}.json')
    
    # Save username to file
    with open(f'{database_directory}/projects/LoggedIn.txt', 'a') as f:
        f.write(project + '\n')
    
    # Remove LoggedIn Accounts from BadPassword, TwoFactorRequired, ChallengeRequired, ChallengeUnknownStep, Cancelled
    exec(open(f"{python_directory}/modules/LoggedIn.py").read())
    
    # Print Login Status
    print(f"[Account Login Successfully: {project}]")
except BadPassword:
    # Handle BadPassword Exception
    exec(open(f"{python_directory}/modules/BadPassword.py").read())
except TwoFactorRequired:
    # Handle TwoFactorRequired Exception
    exec(open(f"{python_directory}/modules/TwoFactorRequired.py").read())
except ChallengeRequired:
    # Handle ChallengeRequired Exception
    exec(open(f"{python_directory}/modules/ChallengeRequired.py").read())
except ChallengeUnknownStep:
    # Handle ChallengeUnknownStep Exception
    exec(open(f"{python_directory}/modules/ChallengeUnknownStep.py").read())
except UnknownError:
    # Handle UnknownError Exception
    exec(open(f"{python_directory}/modules/UnknownError.py").read())
except Exception as e:
    print(f"Failed to Login: {e}")

