# 嵌套
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 创建一个空列表
aliens = []
# 创建30个绿外星人
for alien_num in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)
# 将前三个属性做修改
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
print("\nTotal number of aliens: " + str(len(aliens)))

# 字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppiings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())