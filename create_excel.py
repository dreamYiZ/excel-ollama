import pandas as pd
import os
from faker import Faker

# 创建一个Faker实例
fake = Faker()

# 创建四个空的DataFrame
df_attendance = pd.DataFrame()
df_sales = pd.DataFrame()
df_purchase = pd.DataFrame()
df_revenue = pd.DataFrame()

# 添加一些员工和日期
df_attendance['员工'] = [fake.name() for _ in range(1000)]
df_attendance['日期'] = [fake.date_between(start_date='-1y', end_date='today').strftime('%Y%m%d') for _ in range(1000)]
df_attendance['考勤状态'] = [fake.random_element(elements=('出勤', '请假', '迟到', '早退')) for _ in range(1000)]

# 添加销售记录
df_sales['日期'] = [fake.date_between(start_date='-1y', end_date='today').strftime('%Y%m%d') for _ in range(1000)]
df_sales['销售额'] = [fake.random_int(min=1000, max=5000) for _ in range(1000)]
df_sales['产品'] = [fake.random_element(elements=('水壶', '日历', '塑料花', '水杯', '牙刷子')) for _ in range(1000)]

# 添加采购记录
df_purchase['日期'] = [fake.date_between(start_date='-1y', end_date='today').strftime('%Y%m%d') for _ in range(1000)]
df_purchase['采购额'] = [fake.random_int(min=500, max=2500) for _ in range(1000)]
df_purchase['产品'] = [fake.random_element(elements=('水壶', '日历', '塑料花', '水杯', '牙刷子')) for _ in range(1000)]

# 添加营业收入记录
df_revenue['日期'] = [fake.date_between(start_date='-1y', end_date='today').strftime('%Y%m%d') for _ in range(1000)]
df_revenue['营业收入'] = [fake.random_int(min=5000, max=10000) for _ in range(1000)]
df_revenue['产品'] = [fake.random_element(elements=('水壶', '日历', '塑料花', '水杯', '牙刷子')) for _ in range(1000)]

# 创建文件路径
file_path_attendance = os.path.join('data', '出勤记录表.xlsx')
file_path_sales = os.path.join('data', '销售记录表.xlsx')
file_path_purchase = os.path.join('data', '采购表.xlsx')
file_path_revenue = os.path.join('data', '营业收入表.xlsx')

# 将DataFrame保存为Excel文件
df_attendance.to_excel(file_path_attendance, index=False)
df_sales.to_excel(file_path_sales, index=False)
df_purchase.to_excel(file_path_purchase, index=False)
df_revenue.to_excel(file_path_revenue, index=False)
