# 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 列表索引,索引从0开始
print(bicycles[0])
print(bicycles[1].title())

# 索引可以是负数，从-1开始
print(bicycles[-1])

# 使用列表中的值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)