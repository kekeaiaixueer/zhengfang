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
# 登录教务系统的函数
def login_school(url, username, password):
    school_client = SchoolClient(url)
    return school_client.user_login(username, password)

# 登录后从教务系统获取个人信息的函数
def get_personal_info(school_login):
    info = school_login.get_info()
    name = info['real_name']
    faculty = info['faculty']
    return name, faculty

# 获取指定学年和学期的成绩的函数
def get_scores(school_login, year, term):
    return school_login.get_score(score_year=year, score_term=term)

# 将个人信息和成绩格式化为文本字符串的函数
def format_score_info(name, faculty, scores):
    info_text = f'个人信息:\n姓名:{name}\n院系:{faculty}\n相关分数\n'
    for course in scores:
        info_text += (
            f"\n科目: {course['lesson_name']}\n"
            f"成绩: {course['score']}\n"
            f"------"
        )
    return info_text

def load_key():
    return open('secret', 'rb').read()

# 使用Fernet进行加密
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# 使用Fernet进行解密
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# 修改写入文件的函数，使用加密
def write_to_file(file_path, content, mode='wb'):  # 注意模式改为'wb'因为加密后的数据是字节类型
    encrypted_content = encrypt_message(content)
    with open(file_path, mode) as file:
        file.write(encrypted_content)

# 修改读取文件的函数，使用解密
def read_file(file_path):
    with open(file_path, 'rb') as file:  # 注意模式改为'rb'因为加密后的数据是字节类型
        encrypted_content = file.read()
    return decrypt_message(encrypted_content)

# 使用PushPlus发送通知的函数
def send_update_notification(token, message):
    send_message('成绩', message, token)

# 主函数，负责协调脚本的运行流程
def main():
    # 登录教务系统
    school_login = login_school(URL, USERNAME, PASSWORD)
    # 获取个人信息
    name, faculty = get_personal_info(school_login)
    # 获取成绩
    scores = get_scores(school_login, YEAR, TERM)
    # 格式化信息和成绩为文本字符串
    info_text = format_score_info(name, faculty, scores)
    
    # 将新数据写入临时文件
    write_to_file(NEW_DATA_FILE, info_text)
    
    # 从数据文件中读取当前的数据
    source_content = read_file(DATA_FILE)
    # 从临时文件中读取新的数据
    new_content = read_file(NEW_DATA_FILE)
    
    # 比较当前数据和新数据
    if source_content != new_content:
        # 如果数据不同，更新数据文件并发送通知
        print("内容不同，已更新")
        write_to_file(DATA_FILE, new_content)
        send_update_notification(TOKEN, info_text)
    else:
        # 如果数据相同，则不需要更新
        print("内容相同，不更新")
    
    # 在处理完毕后清空临时新数据文件的内容
    write_to_file(NEW_DATA_FILE, '')

# 该块确保只有在直接运行脚本时才调用main函数
if __name__ == '__main__':
    main()
