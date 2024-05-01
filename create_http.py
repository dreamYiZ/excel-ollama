import http.server
import socketserver
import os


def start_server():
    # 定义服务器的端口
    PORT = 8000

    # 更改工作目录到 'output' 文件夹
    os.chdir("output")

    # 创建一个请求处理器
    Handler = http.server.SimpleHTTPRequestHandler

    # 使用socketserver创建一个服务器
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("\n")
        print(f"服务启动在端口 {PORT}，请在浏览器中打开 http://localhost:{PORT}")
        httpd.serve_forever()
