import requests
import json

def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
