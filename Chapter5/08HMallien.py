# 5-3 Practice
alien_colors = ['green', 'yellow', 'red']
alien_color = "green"
if alien_color == "green":
    print("玩家获得5个点")

if alien_color == "red":
    print("玩家获得5个点")

# 5-4 Practice
alien_color = "green"
if alien_color == "green":
    print("由于射杀外星人，获得5个点")
else:
    print("玩家获得10个点")

# 5-5 Practice
if alien_color == "green":
    print("由于射杀外星人，获得5个点")
elif alien_color == "yellow":
    print("玩家获得10个点")
elif alien_color == "red":
    print("玩家获得15个点")

# 5-6 Practice
age = 18
if age < 2:
    print("This is a baby.")
elif age < 4:
    print("正在蹒跚学步。")
elif age < 13:
    print("是儿童")
elif age < 20:
    print("是青少年。")
elif age < 65:
    print("是成年人。")
else:
    print("是老年人。")

# 5-7 Practice
favorite_fruits = ['apple', 'pear', 'banana']
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'pear' in favorite_fruits:
    print("You really like pear!")
if 'banana' in favorite_fruits:
    print("You really like banana!")
if "pineapple" in favorite_fruits:
    print("You really like pineapple!")
if "orange" in favorite_fruits:
    print("You really like orange!")