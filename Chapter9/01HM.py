# 9-1 Practice
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name +
              " and cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("This restaurant is open!")

hongxing = Restaurant('hongxing', 'Sichuan cuisine')
print(hongxing.restaurant_name)
print(hongxing.cuisine_type)
hongxing.describe_restaurant()
hongxing.open_restaurant()

# 9-2 Practice
res1 = Restaurant('老酒川菜坊', 'Sichuan cuisine')
res2 = Restaurant('绿茶餐厅', 'Jiangsu and Zhejiang cuisine')
res3 = Restaurant('食萃楼', 'Shandong cuisine')

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()

# 9-3
class User():

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("This User is " + full_name + " and age is " +
              str(self.age) + ".")

    def greet_user(self):
        print("Hi " + self.first_name + "~")

user_1 = User('Royal', 'Lee', 'man', 18)

user_1.describe_user()