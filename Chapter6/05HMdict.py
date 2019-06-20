# 6-4 Practice
word_dict = {
    'if': "如果",
    'else': "其他情况",
    'for': '有限循环',
    'while': '无限循环',
    'raise': '抛出异常',
    'try': '捕获异常',
    'catch': '处理异常',
    'finally': '捕获异常之后',
    'def': '函数',
    'break': '停止'
}
for k, v in word_dict.items():
    print(k + ": " + v)

# 6-5 Practice
rivers = {
    'amazon river': 'Brazil',
    'nile': 'egypt',
    'Yangtze River': 'China'
}
for k, v in rivers.items():
    print("The " + k.title() + " runs through " + v.title())
for k in rivers:
    print(k.title())
for v in rivers.values():
    print(v.title())

# 6-6 Practice
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
users = ['henry', 'jenny', 'edward', 'jen']
for user in users:
    if user.lower() in list(i.lower() for i in favorite_languages.keys()):
        print(user.title() + " Thank you for being polled.")
    else:
        print(user.title() + " Please take our poll.")