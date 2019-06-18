# 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

# 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# 复制列表 使用[:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)