# 10-6 Practice
try:
    number1 = input("请输入第一个数字：")
    print(int(number1))

    number2 = input("请输入第二个数字：")
    print(int(number2))
except ValueError:
    print("输入的数字不是整数，请输入数字。")

# 10-7 Practice
while True:
    try:
        number1 = input("请输入第一个数字：")
        print(int(number1))

        number2 = input("请输入第二个数字：")
        print(int(number2))
    except ValueError:
        print("输入的数字不是整数，请输入数字。")

# 10-8 Practice
pet_list = ["cats.txt", "dogs.txt"]

for list in pet_list:
    try:
        with open(list) as f:
            for line in f:
                print(line.strip())
        print("----------")

    except FileNotFoundError:
        # print("There is not " + list + " here.")
        pass

# 10-9 Practice pass

# 10-10 Practice
with open('El Protestantismo.txt') as f:
    contents = f.read()
    count = contents.lower().count('the')
    print(count)