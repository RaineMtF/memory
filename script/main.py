import os
import download
import getcard

def m_format(content):
    card = [
        getcard.getcardl(0),
        getcard.getcardr(0),
        getcard.getcardl(1),
        getcard.getcardl(2),
        getcard.getcardr(1),
        getcard.getcardr(2)
    ]

    def m_get(id):
        return [''] + list(map(lambda i : i['id'], card[:6]))

    return content.format(
        subtitle = "小标题",
        name = m_get('name'),
        name_eng = m_get('name_eng'),
        remark = m_get('remark'),
        nickname = m_get('nickname'),
        nickname_eng = m_get('nickname_eng'),
        date = m_get('date'),
        countdown = m_get('countdown'),
        region = m_get('region'),
        region_eng = m_get('region_eng'),
        img = m_get('img')
    ) + "\n\n<!-- 这个页面是自动生成的 -->"

def Main():
    # download.Main()

    file_path = '../src/index.html'
    backup_path = '../src/index.html.bak'

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    os.rename(file_path, backup_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(m_format(content))
    print("文件处理完成")

if __name__ == "__main__":
    Main()
