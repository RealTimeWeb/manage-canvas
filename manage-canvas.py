import json
import os
import requests
import argparse

SETTINGS_PATH = 'settings.json'

settings = {
    'courses': {},
    'token': 0
}

# Create settings file if it doesn't exist
if not os.path.exists(SETTINGS_PATH):
    with open(SETTINGS_PATH, 'w') as settings_file:
        json.dump(settings, settings_file)

# Load in the settings file
with open(SETTINGS_PATH) as settings_file:
    new_settings = json.load(settings_file)
    settings.update(new_settings)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage canvas courses')
    parser.add_argument('command', help='A command to run')
    
    