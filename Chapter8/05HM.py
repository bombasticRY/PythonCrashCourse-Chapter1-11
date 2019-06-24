# 8-12 Practice
def make_sandwich(*toppings):
    for topping in toppings:
        print("- " + topping)

make_sandwich('ham')
make_sandwich('ham', 'vegetables')

# 8-13 Practice
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Royal', 'Lee',
                             location='beijing',
                             work='IT',
                             age=18)
print(user_profile)

# 8-14 Practice
def car_info(name, type, **info):
    car_info_dict = {}
    car_info_dict['name'] = name
    car_info_dict['type'] = type
    for k, v in info.items():
        car_info_dict[k] = v
    return car_info_dict
print(car_info('subaru', 'outback', color='blue', tow_package=True))