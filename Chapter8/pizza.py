# 任意数量的实参 （创建了空元组）
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合位置实参与任意数量参数
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print('- ' + topping)

make_pizza(16, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')