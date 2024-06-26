import json
import platform

try:
    with open("C:/blackaquapydroid/modules/config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    with open("/storage/emulated/0/blackaquapydroid/modules/config.json") as f:
        config = json.load(f)

# Determine current platform
current_platform = platform.system().lower()

# Get file paths based on platform
if current_platform == 'windows':
    file_paths = config['windows']
elif current_platform == 'linux':
    file_paths = config['linux']
else:
    raise Exception("Unsupported platform")

# Access file paths
python_directory = file_paths['python_directory']
database_directory = file_paths['database_directory']
local_directory = file_paths['local_directory']

# Example usage
print("Python directory:", python_directory)
print("Database directory:", database_directory)
print("Local directory:", local_directory)
