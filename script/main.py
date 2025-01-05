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

    name = ['']
    for i in range(0, 6):
        name.append(card[i]['name'])

    remark = ['']
    for i in range(0, 6):
        remark.append(card[i]['remark'])

    nickname = ['']
    for i in range(0, 6):
        nickname.append(card[i]['nickname'])

    date = ['']
    for i in range(0, 6):
        date.append(card[i]['date'])

    countdown = ['']
    for i in range(0, 6):
        countdown.append(card[i]['countdown'])

    region = ['']
    for i in range(0, 6):
        region.append(card[i]['region'])

    img = ['']
    for i in range(0, 6):
        img.append(card[i]['img'])

    return content.format(
        subtitle = "小标题",
        name = name,
        remark = remark,
        nickname = nickname,
        date = date,
        countdown = countdown,
        region = region,
        img = img
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
