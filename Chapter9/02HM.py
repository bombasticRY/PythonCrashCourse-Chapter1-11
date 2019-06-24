# 9-4 Practice
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name +
              " and cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("This restaurant is open!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

res1 = Restaurant('hongxing', 'Sichuan Cuisine')
print(res1.number_served)

res1.set_number_served(12)
print(res1.number_served)

res1.increment_number_served(10)
print(res1.number_served)

# 9-5 Practice
class User():

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("This User is " + full_name + " and age is " +
              str(self.age) + ".")

    def greet_user(self):
        print("Hi " + self.first_name + "~")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user0 = User('Daisy', 'Duan', 'female', 22)
print(user0.login_attempts)
user0.increment_login_attempts()
print(user0.login_attempts)
user0.increment_login_attempts()
user0.increment_login_attempts()
user0.increment_login_attempts()
print(user0.login_attempts)
user0.reset_login_attempts()
print(user0.login_attempts)