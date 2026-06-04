```
# -*- coding:utf-8 -*-
import tkinter as tk
import requests
import hashlib
import random
import json

youdao_url = 'https://openapi.youdao.com/api'
app_key = '***已隐藏***'
app_secret = '***已隐藏***'


root_window = tk.Tk()
root_window.title('翻译工具')
root_window.geometry('450x300')

tk.Label(root_window, text="请输入要翻译的文字").pack(pady=10)

input_text = tk.StringVar()
tk.Entry(root_window, width=50, textvariable=input_text).pack(pady=5)

tk.Label(root_window, text="翻译结果").pack(pady=10)


frame = tk.Frame(root_window, bg='red', width=400, height=100)
frame.pack(pady=10)
frame.pack_propagate(0)


result = tk.StringVar()
result_label = tk.Label(frame, textvariable=result, width=50, height=6, bg="white", anchor="nw", justify="left")
result_label.pack(padx=5, pady=5)


def create_sign(q, app_key, app_secret, salt):
    sign = app_key + q + salt + app_secret
    return hashlib.md5(sign.encode('utf-8')).hexdigest()


def translate_text(*args):
    try:
        q = input_text.get()
        if not q:
            raise ValueError("请输入文本进行翻译")

        salt = str(random.randint(32768, 65536))
        sign = create_sign(q, app_key, app_secret, salt)

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'q': q,
            'from': 'auto',
            'to': 'zh-CHS',
            'appKey': app_key,
            'salt': salt,
            'sign': sign,
        }

        response = requests.post(youdao_url, headers=headers, data=data)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            if 'translation' in response_data:
                result.set(response_data['translation'][0])
            else:
                result.set("翻译失败，请检查输入或网络连接。")
        else:
            result.set("请求失败，状态码：" + str(response.status_code))
    except Exception as e:
        result.set("翻译失败，请检查输入或网络连接。")


B = tk.Button(root_window, text="翻译", command=translate_text)
B.pack(pady=10)

# 开启主循环，让窗口处于显示状态
root_window.mainloop()
```



