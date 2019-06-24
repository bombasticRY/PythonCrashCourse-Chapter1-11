# 9-10 Practice
from Chapter9.restaurant import Restaurant as res

res1 = res("barbeecue", 'Northeast Cuisine')
res1.describe_restaurant()

# 9-11 Practice
from Chapter9.user import Admin

admin = Admin("Haitang", 'Shangguan', 'female', 25)
admin.privileges1.show_privileges()

# 9-12 Practice
from Chapter9.admin import Admin

admin1 = Admin("Shifei", 'Cheng', 'male', 26)
admin1.show_privileges()