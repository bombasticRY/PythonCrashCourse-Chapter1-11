def describe_pet(animal_type, pet_name):
    print("\nI hava a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat', 'mimi')
describe_pet('dog', 'willie')

# 关键字传值
describe_pet(animal_type='hamster', pet_name='harry')

# 默认值 有默认值的形参在后面
def describe_pet(pet_name, animal_type='dog'):
    print("\nI hava a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(animal_type='hamster', pet_name='harry')