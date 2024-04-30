import pandas as pd
import os
from faker import Faker

# 创建一个Faker实例
fake = Faker()

# 创建一个空的DataFrame
df = pd.DataFrame()

# 添加一些员工和日期
df['员工'] = [fake.name() for _ in range(1000)]
df['日期'] = [fake.date_between(start_date='-1y', end_date='today') for _ in range(1000)]

# 添加考勤状态
df['考勤状态'] = [fake.random_element(elements=('出勤', '请假', '迟到', '早退')) for _ in range(1000)]

# 创建文件路径
file_path = os.path.join('data', '考勤表.xlsx')

# 将DataFrame保存为Excel文件
df.to_excel(file_path, index=False)