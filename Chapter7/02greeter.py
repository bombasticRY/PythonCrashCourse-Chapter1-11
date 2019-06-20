name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who your are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, " + name + "!")

# 使用int来获取输入
age = input("How old are you? ")
age = int(age)
print(age > 18)