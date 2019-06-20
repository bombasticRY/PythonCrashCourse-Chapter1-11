# 6-1 Practice
name = {
    'first_name': 'Thor',
    'last_name': 'Odinson',
    'age': 5000,
    'city': 'Asgard'
}
print(name)

# 6-2 Practice
favorite_nums = {
    'Thor': 5,
    'Loki': 20,
    'Odin': 800,
    'Tony': 3000,
    'Fury': 10001
}
print(favorite_nums)
print("Tony, Is your favorite number 5?")
if favorite_nums['Tony'] == 5:
    print("Yes!")
else:
    print("Sorry, it's not.")

# 6-3 Practice
word_dict = {
    'if': "如果",
    'else': "其他情况",
    'for': '有限循环',
    'while': '无限循环',
    'raise': '抛出异常'
}

print("if: " + word_dict['if'])
print("else: " + word_dict['else'])
print("for: " + word_dict['for'])
print("while: " + word_dict['while'] + "\nraise: " + word_dict['raise'])