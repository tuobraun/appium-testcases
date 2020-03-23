import os
import json
import sys


def load_config(platform='iOS'):
    with open('Application/desired_caps.json', 'r') as f:
        json_data = json.load(f)        
        json_caps = json_data["iOS"] if platform == 'iOS' else json_data["Android"]
    print(f'Configuration file is loaded for: {platform}')
    return json_caps
