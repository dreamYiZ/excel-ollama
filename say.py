import requests
import json
import os
from datetime import datetime

def say(prompt, model="llama3"):
    data = {
        "model": model,
        "prompt": prompt,
    }

    url = "http://localhost:11434/api/generate"

    # 发送POST请求
    response = requests.post(url, data=json.dumps(data))

    response_texts = response.text.split("\n")

    # 解析每个JSON对象
    response_jsons = [
        json.loads(response_text) for response_text in response_texts if response_text
    ]

    output_str = ""
    # 打印返回的数据
    for response_json in response_jsons:
        output_str += response_json["response"]

    print(output_str)

    output_json = {"data": [{"type": "excel", "data": output_str}]}

    # 获取当前时间
    now = datetime.now()

    # 格式化时间字符串，用于生成文件名
    time_str = now.strftime("%Y%m%d%H%M%S")

    # 创建文件路径
    file_path = os.path.join("output", f"data_{time_str}.json")

    # 将output_json保存为JSON文件
    with open(file_path, "w") as json_file:
        json.dump(output_json, json_file, ensure_ascii=False)

    return output_str