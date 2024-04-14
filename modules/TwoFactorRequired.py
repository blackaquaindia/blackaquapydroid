# If login is successful, do something
print("Two-factor authentication required (you did not provide verification_code for login method)")

# If login fails due to bad password, save the username to a file
with open(f"{database_directory}/projects/TwoFactorRequired.txt", "a") as f:
    f.write(project + '\n')

try:
    # Remove Line from LoggedIn, BadPassword, Locked, UnknownError
    filenames = [f"{database_directory}/projects/LoggedIn.txt", f"{database_directory}/projects/BadPassword.txt", f"{database_directory}/projects/Locked.txt", f"{database_directory}/projects/UnknownError.txt"]
    for filename in filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        with open(filename, 'w') as f:
            [f.write(l) for l in lines if l.strip() != project]
except Exception as e:
    pass
