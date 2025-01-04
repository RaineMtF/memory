import os
import download
import getcard

def m_format(content):
    # 在此处实现你的处理逻辑
    card = []
    for i in range(0, 3):
        card.append(getcard.getcardl(i))
    for i in range(0, 3):
        card.append(getcard.getcardr(i))
    img = [getcard.getimgl(), getcard.getimgr()]
    return content.format(
        subtitle = "小标题",
        card1 = card[0],
        card2 = card[1],
        card3 = card[2],
        card4 = card[3],
        card5 = card[4],
        card6 = card[5],
        card1img = img[0],
        card2img = img[1]
    ) + "\n\n<!-- 这个页面是自动生成的 -->"

def Main():
    download.Main()

    file_path = '../src/index.html'
    backup_path = '../src/index.html.bak'

    try:
        os.remove(backup_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        os.rename(file_path, backup_path)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(m_format(content))
        print("文件处理完成")
    except Exception as e:
        print(f"处理文件时出错: {e}")

if __name__ == "__main__":
    Main()
