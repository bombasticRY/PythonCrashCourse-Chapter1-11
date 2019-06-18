# 4-3 Practice
for i in range(1, 21):
    print(i)

# 4-4 Practice
# num_list = [value for value in range(1, 1000001)]
# for i in num_list:
#     print(i)

# 4-5 Practice
num_list = [i for i in range(1, 1000001)]
print(min(num_list))
print(max(num_list))
print(sum(num_list))

# 4-6 Practice
num_list = [i for i in range(1, 21, 2)]
for i in num_list:
    print(i)

# 4-7 Practice
num_list = [i for i in range(3, 31, 3)]
for i in num_list:
    print(i)

# 4-8 Prctice
num_list = []
for value in range(1, 11):
    num_list.append(value ** 3)
for value in num_list:
    print(value)

# 4-9 Practice
num_list = [value ** 3 for value in range(1, 11)]
print(num_list)