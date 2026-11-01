# -*- coding: utf-8 -*-
import http.server
import socketserver
import socket
import os

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

ip = get_local_ip()
url_mobile = f"http://{ip}:{PORT}/mobile.html"
url_desktop = f"http://{ip}:{PORT}/index.html"

print("=" * 60)
print("🚀 考研英语二核心词背诵系统 - 手机局域网局域服务已启动！")
print("=" * 60)
print("请确保手机与电脑连接在【同一个 Wi-Fi】或【手机开启的热点】下：")
print()
print(f"📱 手机端访问地址:   {url_mobile}")
print(f"💻 电脑端访问地址:   {url_desktop}")
print()
print("在手机浏览器（Safari / Chrome / 夸克 / 微信）中直接输入上方手机网址即可！")
print("按 Ctrl + C 可停止服务。")
print("=" * 60)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止。")
