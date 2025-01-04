import os
import requests

def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"文件已下载并保存为: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"下载文件时出错: {e}")

def combine(hide, birthday, people):
    print(hide, birthday, people)

def Main():
    download_file('https://github.com/one-among-us/data/raw/refs/heads/main/data/hdata.json', 'hide.json')
    download_file('https://github.com/one-among-us/data/raw/refs/heads/gh-pages/birthday-list.json', 'birthday.json')
    download_file('https://github.com/one-among-us/data/raw/refs/heads/gh-pages/people-list.json', 'people.json')
    combine('hide.json', 'birthday.json', 'people.jspn')
    os.remove('hide.json')
    os.remove('birthday.json')
    os.remove('people.jspn')

if __name__ == "__main__":
    Main()
