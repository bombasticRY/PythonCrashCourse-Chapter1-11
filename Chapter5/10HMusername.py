# 5-8 Practice
user_names = ['admin', 'hanmeimei', 'lilei', 'Jenny', 'Danny']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user_name +", thank you for logging in again.")

# 5-9 Practice
user_names.clear()
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user_name + ", thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10 Practice
current_users = ['admin', 'hanmeimei', 'lilei', 'JENNY', 'Danny']
new_users = ['Eric', 'Alice', 'Jenny', 'Danny', 'Eli']
for new_user in new_users:
    if new_user.lower() in list(value.lower() for value in current_users):
        print("此用户名已被占用，请输入别的用户名。")
    else:
        print("此用户名未被使用。")

# 5--11
num_list = list(num for num in range(1, 10))
for num in num_list:
    print(num)

for num in num_list:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num ==3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")

# 5-12 Practice
# 审核编码格式
# 5-13 Practice
# 自己的想法与总结