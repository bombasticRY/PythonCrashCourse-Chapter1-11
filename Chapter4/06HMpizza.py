# 4-10 Practice
num_list = [i for i in range(1, 21, 2)]
print("The first three items in the list are:")
for i in num_list[:3]:
    print(i)

print("\nThe items form the middle of the list are:")
for i in num_list[2:5]:
    print(i)

print("\nThe last three items in the list are:")
for i in num_list[-3:]:
    print(i)

# 4-11 Practice
pizzas = ['pepperoni', 'Hawaiian', 'New Orleans', 'Black Pepper Beef']
friend_pizzas = pizzas[:]

pizzas.append("pizzaA")
friend_pizzas.append("pizzaB")
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12 Practice
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for i in my_foods:
    print(i)
print("---------------")
for i in friend_foods:
    print(i)