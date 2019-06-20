# 6-7 Practice
name_0 = {
    'first_name': 'Thor',
    'last_name': 'Odinson',
    'age': 5000,
    'city': 'Asgard'
}
name_1 = {
    'first_name': 'Loki',
    'last_name': 'Odinson',
    'age': 4800,
    'city': 'Asgard'
}
name_2 = {
    'first_name': 'Odin',
    'last_name': 'Borrson',
    'age': 9800,
    'city': 'Asgard'
}
names = [name_0, name_1, name_2]
for name in names:
    print(name)

# 6-8 Practice
mimi = {
    'type': 'cat',
    'master': "Thor",
}
doge = {
    'type': 'dog',
    'master': 'Loki',
}
woli = {
    'type': 'wolf',
    'master': 'Odin'
}
pets = [mimi, doge, woli]
for pet in pets:
    print(pet)

# 6-9 Practice
favorite_places = {
    'Thor': ['Earth', 'Mars', 'Moon'],
    'Loki': ['Earth', 'Asgard'],
    'Odin': ['Asgard'],
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(name.title() + "'s favourite place is:")
    else:
        print(name.title() + "'s favourite places are:")
    for place in places:
        print("\t" + place)

# 6-10 Practice
favorite_nums = {
    'Thor': [5],
    'Loki': [20, 52],
    'Odin': [800, 945, 444],
    'Tony': [3000, 8],
    'Fury': [10001, 20000, 65321, 98554],
}
for name, numbers in favorite_nums.items():
    if len(numbers) == 1:
        print(name.title() + "'s favourite number is:")
    else:
        print(name.title() + "'s favourite numbers are:")
    for number in numbers:
        print("\t" + str(number))

# 6-11 Practice
cities = {
    'beijing': {
        'country': 'China',
        'population': 35000000,
        'fact': 'Capital of China'
    },
    'paris': {
        'country': 'French',
        'population': 4000000,
        'fact': 'Romantic Capital in the world'
    },
    'tokyo': {
        'country': 'Japan',
        'population': 19000000,
        'fact': "It's hot there"
    }
}
for city, ob in cities.items():
    print(city.title())
    for k, v in ob.items():
        print(k + ": " + str(v))

# 6-12 Practice 扩展 略