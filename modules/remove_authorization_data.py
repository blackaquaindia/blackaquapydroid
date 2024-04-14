# data variable is important function for Removing Authorization Data

import json
try:
    # Load the JSON file
    with open(f'{database_directory}/devices/{project}.json') as f:
        data = json.load(f)
    
    # Remove the "authorization_data" field
    if 'authorization_data' in data:
        del data['authorization_data']
    
    # Remove the "mid" field
    #if 'mid' in data:
        #del data['mid']
    
    # Save the modified JSON file
    with open(f'{database_directory}/devices/{project}.json', 'w') as f:
        json.dump(data, f)
except Exception as e:
    print(f"")
