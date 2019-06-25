# 10-3 Practice
# filename = 'guest.txt'
#
# with open(filename, 'a', encoding='utf-8') as file_object:
#     file_object.write(input("请输入用户名：") + "\n")

# 10-4 Practice
# filename = 'guest_book.txt'
#
# with open(filename, 'a', encoding='utf-8') as file_object:
#     action = True
#     while action:
#         input_str = input("请输入用户名：")
#         if input_str == 'q':
#             break
#         else:
#             print("Hello " + input_str + "! How's it going?")
#             file_object.write(input_str + "\n")

# 10-5 Practice
filename = 'reason_of_programming.txt'

while True:
    input_str = input("请输入编程原因：")
    if input_str == 'q':
        break
    else:
        with open(filename, 'a', encoding='utf-8') as file_object:
            file_object.write(input_str + "\n")