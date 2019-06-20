# 7-4 Practice
message = ""
while True:
    if message == 'quit':
        break
    else:
        message = input("请输入配料： ")
        print("我们将在pizza中加入" + message + "。")

# 7-5 Practice
while True:
    age = input("请问您多大了？(输入quit结束) ")
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            price = 0
        elif int(age) <= 12:
            price = 10
        elif int(age) > 12:
            price = 15
        print("票价为：$" + str(price) + ".")

# 7-6 lue
# 7-7 Practice
while True:
    print(1)