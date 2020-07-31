import os
import json
import sys


def load_config(define_platform):
    with open('Application/desired_caps.json', 'r') as f:
        json_data = json.load(f)
        json_caps = json_data["iOS"] if define_platform == 'iOS' else json_data["Android"]
    print(f'Configuration file is loaded for: {define_platform}')
    return json_caps
