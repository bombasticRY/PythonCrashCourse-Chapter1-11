cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# 条件测试
car = 'bmw'
print(car == 'bmw')

# 不考虑大小写,False
car = 'bmw'
print(car == 'BMW')

car = 'Audi'
print(car.lower() == 'audi')