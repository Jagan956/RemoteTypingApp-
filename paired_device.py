import json
import os

FILE = 'device.json'

def save_device(device_info):
    with open(FILE, 'w') as f:
        json.dump({'device': device_info}, f)

def load_device():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f).get('device')
    return None
