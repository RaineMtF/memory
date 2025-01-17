import os
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

ren = {
    '出生': 'born',
    'Born': 'born',
    '逝世': 'departed',
    'Departed': 'departed',
    '昵称': 'alias',
    'Alias': 'alias',
    '地区': 'location',
    'Location': 'location',
    '年龄': 'age',
    'Age': 'age'
}

def get_json(path):
    info = load_json(f'./data/people/{path}/info.json')
    info_en = load_json(f'./data/people/{path}/info.en.json')

    data = {}
    for item in info['info']:
        data[ren[item[0]]] = item[1]

    data_en = {}
    for item in info_en['info']:
        data_en[ren[item[0]]] = item[1]
    
    def m_get(data_lang, id, none='None'):
        return data_lang[id] if (id in data_lang) else none

    assert m_get(info, 'id') == path

    content = {
        'id': path,
        'name': m_get(info, 'name'),
        'name_en': m_get(info_en, 'name'),
        'alias': m_get(data, 'alias', path),
        'alias_en': m_get(data_en, 'alias', path),
        'born': m_get(data, 'born', None),
        'departed': m_get(data, 'departed', None),
        'age': m_get(data, 'age', 'N/A'),
        'location': m_get(data, 'location', '未知'),
        'location_en': m_get(data_en, 'location', 'Unknown'),
        'avatar': './' + info['profileUrl'].format(path=path)[1:]
    }

    # print(path, content)
    
    return content

def Main():
    content = []
    os.system('git clone https://github.com/one-among-us/data.git --single-branch --branch gh-pages --depth=1')
    for item in load_json('./data/people-home-list.json'):
        content.append(get_json(item['path']))
    # print(content)
    with open('people.json', 'w', encoding='utf-8') as file:
        json.dump(content, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    Main()
