import init
import os
import pandas as pd
import requests
import json

def read_all_excel_files_in_folder(folder_path):
    # 获取文件夹中的所有文件名
    filenames = os.listdir(folder_path)

    # 筛选出Excel文件
    excel_filenames = [filename for filename in filenames if filename.endswith('.xlsx') or filename.endswith('.xls')]

    # 初始化一个字符串来收集信息
    info_text = ""

    # 读取每个Excel文件
    for excel_filename in excel_filenames:
        # 创建文件路径
        file_path = os.path.join(folder_path, excel_filename)

        # 读取Excel文件的所有工作表
        dfs = pd.read_excel(file_path, sheet_name=None)

        # 收集每个工作表的信息
        for sheet_name, df in dfs.items():
            info_text += f"Sheet name: {sheet_name}\n"
            info_text += df.to_string() + "\n\n"  # 使用to_string()方法将DataFrame转换为字符串

    # 返回收集到的信息
    return info_text


if __name__ == '__main__':
    init.hello()
    init.check_system()
    init.pull_model()
    
    # 使用函数
    excel_info_text  = read_all_excel_files_in_folder('data')

    # 定义API的URL
    url = "http://localhost:11434/api/generate"
    
    print(excel_info_text)

    # 定义请求的数据
    data = {
        "model": "llama3",
        "prompt": "所有的回答采用中文，分析这个excel数据，并给出数据报告,这个excel是什么的，其中的数据有什么特点？比如平均值、最高值、最低值。\n"+excel_info_text +"\n" + "。请用中文回答。"
    }
    # 发送POST请求
    response = requests.post(url, data=json.dumps(data))

    # 将返回的数据分割成多个JSON对象
    response_texts = response.text.split("\n")
    
    # 解析每个JSON对象
    response_jsons = [json.loads(response_text) for response_text in response_texts if response_text]

    output_str = ""
    # 打印返回的数据
    for response_json in response_jsons:
        # print(response_json["response"])
        # print(json.dumps(response_json))
        output_str += response_json["response"]
        
    print(output_str)