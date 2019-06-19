requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 比较数字
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again")

# 检查多个条件 and or
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
# 为了可读性，可修改判断语句 (aga_0 >= 21) and (age_1 >= 21)

# 使用or检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# 检查特定值是否在列表
requested_topping = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)