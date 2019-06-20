# 7-8 Practice
sandwich_orders = ['pastrami', 'tuna', 'ham cheese', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I make your " + sandwich + "sandwich.")
print("\nFinished making sandwiches.")
print(finished_sandwiches)

# 7-9 Practice
sandwich_orders = ['pastrami', 'tuna', 'ham cheese', 'pastrami', 'pastrami']
print("pastrami has been sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10 Practice
message = "If you could visit one place in the world, where yould you go? "
act = True
visit_places = {}

while act:
    name = input("your name: ")
    place = input(message)

    visit_places[name] = place

    repeat = input("continue? (yes/no) ")
    if repeat == 'no':
        act = False
print(visit_places)