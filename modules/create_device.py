import csv
import json
import time
import random
from instagrapi import Client

# OPEN DEVICES FILE
with open(f'{python_directory}/android/Devices.csv', 'r') as f:
    # Create CSV reader
    reader = csv.reader(f)
    
    # Store rows in list
    rows = list(reader)
    
    # Count number of rows in file (excluding header row)
    num_rows = len(rows) - 1
    
    # Generate random row index (excluding header row)
    row_index = random.randint(1, num_rows)
    
    # Extract values of cells in randomly selected row
    manufacturer = rows[row_index][0]
    model = rows[row_index][1]
    device = rows[row_index][2]
    chipset = rows[row_index][3]
    dpi = rows[row_index][4]
    resolution = rows[row_index][5]
    
    # Print extracted values
    print(f'Manufacturer: {manufacturer}')
    print(f'Model: {model}')
    print(f'Device: {device}')
    print(f'Chipset: {chipset}')
    print(f'DPI: {dpi}')
    print(f'Resolution: {resolution}')



# OPEN ANDROID VERSIONS FILE
with open(f'{python_directory}/android/Android_Versions.csv', 'r') as f:
    # Create CSV reader
    reader = csv.reader(f)
    
    # Store rows in list
    rows = list(reader)
    
    # Count number of rows in file (excluding header row)
    num_rows = len(rows) - 1
    
    # Generate random row index (excluding header row)
    row_index = random.randint(1, num_rows)
    
    # Extract values of cells in randomly selected row
    androidapi = rows[row_index][1]
    androidversion = rows[row_index][2]
    
    # Print extracted values
    print(f'Android API: {androidapi}')
    print(f'Android Version: {androidversion}')



# OPEN ANDROID VERSIONS FILE
with open(f'{python_directory}/android/Instagram_Versions.csv', 'r') as f:
    # Create CSV reader
    reader = csv.reader(f)
    
    # Store rows in list
    rows = list(reader)
    
    # Count number of rows in file (excluding header row)
    num_rows = len(rows) - 1
    
    # Generate random row index (excluding header row)
    row_index = random.randint(1, num_rows)
    
    # Extract values of cells in randomly selected row
    instagramversion = rows[row_index][0]
    igappversion = rows[row_index][1]
    
    # Print extracted values
    print(f'Instagram Version: {instagramversion}')
    print(f'IG App Version: {igappversion}')



# Read file content
with open(f'{python_directory}/android/Custom_Device_Settings_OG.json', 'r') as f:
    file_content = f.read()

# Replace keywords with variables
file_content = file_content.replace('[manufacturer]', manufacturer.strip())
file_content = file_content.replace('[model]', model.strip())
file_content = file_content.replace('[device]', device.strip())
file_content = file_content.replace('[chipset]', chipset.strip())
file_content = file_content.replace('[dpi]', dpi.strip())
file_content = file_content.replace('[resolution]', resolution.strip())

file_content = file_content.replace('[androidapi]', androidapi.strip())
file_content = file_content.replace('[androidversion]', androidversion.strip())

file_content = file_content.replace('[instagramversion]', instagramversion.strip())
file_content = file_content.replace('[igappversion]', igappversion.strip())

# Write modified content back to file
with open(f'{local_directory}/000newdevice.json', 'w') as f:
    f.write(file_content)


# create a client object
cl = Client()

# load device settings from file
cl.load_settings(f'{local_directory}/000newdevice.json')

# Get device settings information
device_settings = cl.get_settings()

# Save device settings to a file
with open(f'{database_directory}/devices/{project}.json', 'w') as f:
    json.dump(device_settings, f)

# Wait for the session to be fully initialized
print(f"Device Created Successfully: {project}")
time.sleep(3)
