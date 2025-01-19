import os
import getcard
from datetime import datetime

def m_format(content):
    card = [
        getcard.getcard_d(0),
        getcard.getcard_b(0),
        getcard.getcard_d(1),
        getcard.getcard_d(2),
        getcard.getcard_b(1),
        getcard.getcard_b(2)
    ]

    def m_get(id):
        return [''] + [i[id] for i in card]

    return content.format(
        subtitle = f"此页面于 {str(datetime.now())} 生成",
        timestamp = datetime.now().strftime("%Y-%m-%d"),
        name = m_get('name'),
        name_en = m_get('name_en'),
        id = m_get('id'),
        alias = m_get('alias'),
        alias_en = m_get('alias_en'),
        date = m_get('date'),
        age = m_get('age'),
        countdown = m_get('countdown'),
        location = m_get('location'),
        location_en = m_get('location_en'),
        avatar = m_get('avatar')
    ) + "\n\n<!-- 这个页面是自动生成的 -->"

def Main():
    print(datetime.now())

    file_path = '../src/index.html'
    backup_path = '../src/index.html.bak'

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    os.rename(file_path, backup_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(m_format(content))
    print("文件处理完成")
    
    os.remove(backup_path)

if __name__ == "__main__":
    Main()
