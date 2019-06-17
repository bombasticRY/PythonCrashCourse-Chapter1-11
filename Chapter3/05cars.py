# 永久升序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 永久降序排序
cars.sort(reverse=True)
print(cars)

# 临时排序sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the Original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# 列表反转(永久)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# 确定列表长度
print(len(cars))