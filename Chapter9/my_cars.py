from Chapter9.electric_car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# 导入整个模块、
import Chapter9.electric_car as ec

my_beetle = ec.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ec.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())