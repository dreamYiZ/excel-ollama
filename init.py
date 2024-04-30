import os
import constant
import psutil


def hello():
    print("START INITIALIZATION ********************************\n********************************\n********************************")

def pull_model():
    os.system(f'ollama pull {constant.MODEL_LLAMA3}')
    # os.system(f'ollama run {constant.MODEL_LLAMA3_70B}')
    
    



def check_system():
    mem_info = psutil.virtual_memory()
    total_memory = mem_info.total / (1024.0 ** 3)
    print(f"Total memory: {total_memory} GB")
    return total_memory