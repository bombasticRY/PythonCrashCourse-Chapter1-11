# 10-11 Practice
import json
# favorite_num = input("请输入你喜欢的数字：")
# filename = "favorite_num.json"
# with open(filename, 'w') as f_obj:
#     json.dump(str(favorite_num), f_obj)
#
# with open(filename) as f_obj:
#     f_n = json.load(f_obj)
#
# print("I know your favorite number, it's " + f_n)

# 10-12 Practice
# filename = "favorite_num.json"
# try:
#     with open(filename) as f_obj:
#         f_n = json.load(f_obj)
# except FileNotFoundError:
#     with open(filename, 'w') as f_obj:
#         favorite_num = input("请输入你喜欢的数字：")
#         json.dump(favorite_num, f_obj)
# else:
#     print("I know your favorite number, it's " + f_n)

# 10-13 Practice
def get_stored_username():
    """如果存储用户名，获取他"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def check_username(username):
    yes_or_no = input("Is that you, " + username + "?(yes or no)")
    if yes_or_no == 'yes':
        return username
    elif yes_or_no == 'no':
        return get_new_username()

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        username = check_username(username)
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()