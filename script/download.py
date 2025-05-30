import os
import common

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
    info = common.load_json(f'./data/people/{path}/info.json')
    info_en = common.load_json(f'./data/people/{path}/info.en.json')

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
        'born': m_get(data, 'born', 'N/A'),
        'departed': m_get(data, 'departed', 'N/A'),
        'age': m_get(data, 'age', 'N/A'),
        'location': m_get(data, 'location', '未知'),
        'location_en': m_get(data_en, 'location', 'Unknown'),
        'avatar': 'https://data.one-among.us/people/' + info['profileUrl'].format(path=path)[1:]
    }

    return content

def Main():
    content = []
    os.system('git clone https://github.com/one-among-us/data.git --single-branch --branch gh-pages --depth=1')
    for item in common.load_json('./data/people-home-list.json'):
        content.append(get_json(item['path']))
    common.write_json('people.json', content)

if __name__ == "__main__":
    Main()
