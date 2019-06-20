# 遍历字典(键值)
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+
          language.title() + '.')

# 遍历字典（键）
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'etin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 遍历字典（按顺序遍历键）
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

# 遍历字典的值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# 为去掉重复的value，将value元素放入set()集合
for language in set(favorite_languages.values()):
    print(language.title())