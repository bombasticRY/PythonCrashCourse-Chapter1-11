magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great show!")

# 忘记缩进的情况会报错
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

# 不必要的缩进也会报错并指出问题所在
# message = "Hello Python world!"
#     print(message)