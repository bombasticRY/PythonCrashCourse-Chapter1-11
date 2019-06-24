# 9-13 Practice
from collections import OrderedDict

word_dict = OrderedDict()
word_dict['if'] = "如果"
word_dict['else'] = "其他情况"
word_dict['for'] = "有限循环"
word_dict['while'] = "无限循环"
word_dict['raise'] = "抛出异常"
word_dict['try'] = "捕获异常"
word_dict['catch'] = "处理异常"
word_dict['finally'] = "捕获异常之后"
word_dict['def'] = "函数"
word_dict['break'] = "停止"
for k, v in word_dict.items():
    print(k + ": " + v)

# 9-14 Practice
from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

six_sides = Die(6)
ten_sides = Die(10)
twenty_sides = Die(20)

for side in range(0, 10):
    print("第" + str(side + 1) + "次： " + str(six_sides.roll_die()))

for side in range(0, 10):
    print("第" + str(side + 1) + "次： " + str(ten_sides.roll_die()))

for side in range(0, 10):
    print("第" + str(side + 1) + "次： " + str(twenty_sides.roll_die()))

# 9-15 Practice
# Python module of the week