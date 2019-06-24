# 9-6 Practice
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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        if len(self.flavors) >= 1:
            for flavor in self.flavors:
                print(flavor)
        else:
            print("No ice cream")

ice_cream1 = IceCreamStand("bling", "Zhejiang Cuisine", ['tudou', 'naiyou', 'hei'])
ice_cream1.show_flavors()

# 9-7 Practice
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


class Privileges():

    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges1 = Privileges()

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

admin = Admin("Tianya", 'Duan', 'male', '27')
admin.show_privileges()

# 9-8 Practice
admin1 = Admin("Yidao", 'Guihai', 'male', 28)
admin1.privileges1.show_privileges()

# 9-9 Practice
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def fill_gas_tank(self):
        print("This car is full of gas.")

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

tang = ElectricCar("tang", 'BYD tang', '2019')
tang.battery.get_range()
tang.battery.upgrade_battery()
tang.battery.get_range()