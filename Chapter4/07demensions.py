# 元组使用（）
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 尝试修改 会报错
# dimensions[0] = 250

# 遍历元组
for dimension in dimensions:
    print(dimension)

# 修改元组变量
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)