import os
from school_api import SchoolClient
from pushplus import send_message
from cryptography.fernet import Fernet
import random
# 脚本的常量设置
URL = os.environ.get("URL")  # 教务系统的URL地址
USERNAME = os.environ.get("USERNAME")       # 登录教务系统的用户名
PASSWORD = os.environ.get("PASSWORD")         # 登录教务系统的密码
YEAR = os.environ.get("YEAR")              # 要查询成绩的学年
TERM = os.environ.get("TERM")                      # 要查询成绩的学期
TOKEN = os.environ.get("TOKEN")  # PushPlus的令牌，用于发送通知
conf = {
    "url": URL,
    "lan_url": URL,
    "proxies": {"http": "http://117.26.41.218:8888"},
    "priority_proxy": False  # 值为True时，则直接使用代理访问lan_url地址
}
school = SchoolClient(**conf)
student=school.user_login(USERNAME,PASSWORD,timeout=10)
schedule_data = student.get_schedule()
print(schedule_data)
