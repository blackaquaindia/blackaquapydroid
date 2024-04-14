import json
try:
    cl.load_settings(f"{database_directory}/devices/{project}.json")
except Exception as e:
    print(f"[Device Settings Failed To Load: {e}]")

