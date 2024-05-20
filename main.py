import init
import os
import pandas as pd
import requests
import json
import say
from bs4 import BeautifulSoup,NavigableString
import create_http
import time  # 在文件开头导入time模块
import shutil


# 定义源文件和目标文件的路径
src_file = 'src/style.css'
dst_file = 'output/style.css'


def read_all_excel_files_in_folder(folder_path):
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # 获取文件夹中的所有文件名
    filenames = os.listdir(folder_path)

    # 筛选出Excel文件
    excel_filenames = [
        filename
        for filename in filenames
        if filename.endswith(".xlsx") or filename.endswith(".xls")
    ]

    # 初始化一个列表来收集信息
    info_list = []

    # 读取每个Excel文件
    for excel_filename in excel_filenames:
        # 创建文件路径
        file_path = os.path.join(folder_path, excel_filename)

        # 读取Excel文件的所有工作表
        dfs = pd.read_excel(file_path, sheet_name=None)

        # 收集每个工作表的信息
        for sheet_name, df in dfs.items():
            # 检查每一列，如果数据类型是日期，就将其转换为字符串
            for col in df.columns:
                if pd.api.types.is_datetime64_any_dtype(df[col]):
                    df[col] = df[col].dt.strftime("%Y-%m-%d")
            info = {
                "文件名": excel_filename,
                "工作表名": sheet_name,
                "数据": df.to_dict(),
            }
            info_list.append(info)

    # 返回收集到的信息
    return info_list




def read_excel_in_data_folder_and_analyze():
    # 使用函数
    excel_info_text_list = read_all_excel_files_in_folder("data")

    excel_opt_list = []

    for excel_info_text in excel_info_text_list:


        # 将字典转换为字符串
        excel_info_text_str = json.dumps(excel_info_text, ensure_ascii=False)

        # 定义请求的数据
        data = {
            "model": "llama3",
            "prompt": f'所有的回答采用中文，这是一个{excel_info_text["文件名"]}-{excel_info_text["工作表名"]}表，请你作为一个专业的数据挖掘分析师和企业管理专家进行分析，并提出企业经营管理建议。\n'
            + excel_info_text_str
            + "\n"
            + "。请用中文回答。",
        }

        # 使用say函数发送请求并获取响应
        output_str = say.say(data["prompt"], model=data["model"])


        excel_opt_list.append(output_str)

        time.sleep(1)  # 在每个请求之间等待1秒

    return excel_opt_list


def main():
    init.hello()
    init.check_system()
    init.pull_model()

    excel_output_str = read_excel_in_data_folder_and_analyze()

    total_excel = ""
    for excel_opt_item in excel_output_str:
        # 定义请求的数据
        total_excel += excel_opt_item

    prompt = (
        "所有的回答采用中文，你是专业的企业管理人员，请对数据分析报告进行总结\n"
        + total_excel
        + "\n"
        + "。请用中文回答。"
    )
    got = say.say(prompt, model="llama3")

    # 你的main_output内容
    main_output = total_excel + "\n" + got

    # 读取HTML文件
    with open("src/index.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    # 找到<main>标签
    main_tag = soup.find("main", class_="main")

    # 按换行符分割main_output
    paragraphs = main_output.split('\n')

    # 用<p>标签包裹每一段，并将其作为HTML插入
    for p in paragraphs:
        new_tag = soup.new_tag("p")
        new_tag.string = NavigableString(p)
        main_tag.append(new_tag)

    # 写回HTML文件
    with open("output/index.html", "w") as file:
        file.write(str(soup))
        
    # 使用shutil.copy()函数复制文件
    shutil.copy(src_file, dst_file)        
        
    create_http.start_server()


if __name__ == "__main__":
    main()
