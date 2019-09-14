"""
handles json read_write functions
"""
import json
from pathlib import Path

def get_lunches():
    data = {}
    path = Path('lunches.json')
    if not path.is_file():
        update_lunches({"data": []})
    with open('lunches.json', 'r') as file:
        data = json.load(file)
    return data

def update_lunches(payload):
    with open('lunches.json', 'w+') as file:
        json.dump(payload, file, indent=2)
