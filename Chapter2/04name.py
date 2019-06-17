name = "ada lovelace"
# 首字母大写
print(name.title())
# 全字母大写
print(name.upper())
# 全字母小写
print(name.lower())

# 合并字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())
print("Hello", full_name.title(), "!")


# 制表符跟换行符添加空白
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language)