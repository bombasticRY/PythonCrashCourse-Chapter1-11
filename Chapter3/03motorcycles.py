motorcycles = ['Honda', 'Yamaha', 'suzuki']
print(motorcycles)

# 修改
motorcycles[0] = 'ducati'
print(motorcycles)

# 末尾添加
motorcycles.append('honda')
print(motorcycles)

# 先创建空列表，在进行插入操作
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 向指定位置插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除del
del motorcycles[0]
print(motorcycles)

# 删除pop(默认从列表末尾删除，栈顶删除，先进后出)
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)

# pop用法
motorcycles = ['Honda', 'Yamaha', 'suzuki']
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print("the last motorcycle I owned was a " + last_owned + ".")
print("the first motorcycle I owned was a " + first_owned + ".")
print(motorcycles)
# 从列表中删除一个元素，且不再以任何形式使用，使用del语句；
# 如果要在删除后继续使用删除元素，使用pop()方法

# remove(不知道索引，只知道值)
motorcycles = ['Honda', 'Yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me")

