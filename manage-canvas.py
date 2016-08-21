import json
import os
import requests
import argparse

SETTINGS_PATH = 'settings.json'

settings = {
    'courses': {},
    'canvas-token': '',
    'canvas-root': 'https://vt.instructure.com/api/v1/'
}

# Create settings file if it doesn't exist
if not os.path.exists(SETTINGS_PATH):
    with open(SETTINGS_PATH, 'w') as settings_file:
        json.dump(settings, settings_file)
        print("A settings.json file was created. Please add your token and courses.")

# Load in the settings file
with open(SETTINGS_PATH) as settings_file:
    new_settings = json.load(settings_file)
    settings.update(new_settings)
    
def get(command, data=None, all=False):
    if data is None:
        data = {}
    data['access_token'] = settings.get('canvas-token')
    if all:
        data['per_page'] = 100
        next_url = settings.get('canvas-url')+command
        final_result = []
        while True:
            response = requests.get(next_url, data=data)
            final_result += response.json()
            if 'next' in response.links:
                next_url = response.links['next']['url']
            else:
                return final_result
    else:
        return requests.get(settings.get('canvas-url')+command, data=data).json()
def post(command, data):
    data['access_token'] = settings.get('canvas-token')
    return requests.post(CANVAS_URL+command, data=data)
def delete(command, data):
    data['access_token'] = settings.get('canvas-token')
    return requests.delete(CANVAS_URL+command, data=data)
def put(command, data):
    data['access_token'] = settings.get('canvas-token')
    return requests.put(CANVAS_URL+command, data=data)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage canvas courses')
    parser.add_argument('command', help='A command to run')
    
    