import os
from school_api import SchoolClient
from pushplus import send_message
from cryptography.fernet import Fernet

# 脚本的常量设置
URL = os.environ.get("URL")  # 教务系统的URL地址
USERNAME = os.environ.get("USERNAME")       # 登录教务系统的用户名
PASSWORD = os.environ.get("PASSWORD")         # 登录教务系统的密码
YEAR = os.environ.get("YEAR")              # 要查询成绩的学年
TERM = os.environ.get("TERM")                      # 要查询成绩的学期
TOKEN = os.environ.get("TOKEN")  # PushPlus的令牌，用于发送通知


DATA_FILE = 'data.txt'          # 存储当前数据的文件
NEW_DATA_FILE = 'new_data.txt'  # 用于存储新数据以便比较的临时文件
school = SchoolClient(URL) 
student = school.user_login(USERNAME,PASSWORD)
student.get_score()
