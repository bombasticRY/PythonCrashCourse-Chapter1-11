def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 让实参变成可选的 (中间名可以不填)
def get_formatted_name(first_name, medium_name, last_name):
    full_name = first_name + " " + medium_name + " " + last_name
    return full_name.title()
# 上述代码改为下面这样即可
def get_formatted_name(first_name, last_name, medium_name=""):
    if medium_name:
        full_name = first_name + " " + medium_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()