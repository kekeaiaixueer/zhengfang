from school_api import SchoolClient
from pushplus import send_message
import os
def login_to_school(url, username, password):
    """
    登录到学校网站。

    参数:
    - url: 学校网站的 URL 地址。
    - username: 学生的用户名。
    - password: 学生的密码。

    返回:
    - user: 登录后的用户对象。
    """
    school = SchoolClient(url)
    user = school.user_login(username, password)
    return user

def get_grade_data(user, year):
    """
    获取指定学年的成绩数据。

    参数:
    - user: 登录后的用户对象。
    - year: 指定的学年。

    返回:
    - data_for_year: 学年的成绩数据。
    """
    schedule_data = user.get_score()
    data_for_year = schedule_data.get(year, {})
    return data_for_year

def format_grade_info(data_for_year):
    """
    格式化成绩信息为一个字符串。

    参数:
    - data_for_year: 学年的成绩数据。

    返回:
    - integrated_grade_info: 格式化后的成绩信息字符串。
    """
    integrated_grade_info = "成绩信息：\n"
    for term, courses in data_for_year.items():
        for course in courses:
            integrated_grade_info += (
                f"\n科目: {course['lesson_name']}\n"
                f"成绩: {course['score']}\n"
                f"------"
            )
    return integrated_grade_info

def send_grade_message(title, message, token):
    """
    使用 PushPlus 发送成绩信息消息。

    参数:
    - title: 消息的标题。
    - message: 消息的内容。
    - token: PushPlus 的 token。
    """
    send_message(title, message, token)

# 使用参数调用函数
url = os.environ.get("URL")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
year = "2023-2024"#学年
TOKEN=os.environ.get("TOKEN")
# 登录学校网站
user = login_to_school(url, username, password)
# 获取成绩数据
data_2023_2024 = get_grade_data(user, year)
# 格式化成绩信息
integrated_grade_info = format_grade_info(data_2023_2024)
# 发送成绩信息消息
send_grade_message('成绩', integrated_grade_info,TOKEN)
