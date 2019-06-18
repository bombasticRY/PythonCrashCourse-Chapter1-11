for value in range(1, 5):
    print(value)

# 使用list()将range结果创建为列表
numbers = list(range(1, 6))
print(numbers)

# 使用range可以指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 将前十个整数的平方放入一个列表中
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 优化上述代码
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 数字列表简单统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)