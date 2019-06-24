# 8-9 Practice
def show_magicians(name_list):
    for name in name_list:
        print(name)

name_list = ['大卫·柯普费尔 ', '刘谦', 'John']
show_magicians(name_list)

# 8-10 Practice
new_name_list = []
def make_great(name_list):
    return list("the Great " + value for value in name_list)

def show_magicians(name_list):
    for name in name_list:
        print(name)

name_list = ['大卫·柯普费尔 ', '刘谦', 'John']
# show_magicians(make_great(name_list))

# 8-11 Practice
new_name_list = []
def make_great(name_list):
    for name in name_list:
        name = "the Great " + name
        new_name_list.append(name)

def show_magicians(name_list):
    for name in name_list:
        print(name)

name_list = ['大卫·柯普费尔 ', '刘谦', 'John']
make_great(name_list)
show_magicians(new_name_list)
show_magicians(name_list)
