# 3-4 Practice
guests = ['郭靖', '杨过', '张无忌', '胡斐']
for person in guests:
    message = "请" + person + "参加今晚的party！"
    print(message)
print("今晚邀请了" + str(len(guests)) + "位嘉宾共进晚餐") # 3-9 Practice

# 3-5 Practice
not_come_guest = guests.pop(0)
print(not_come_guest + "无法赴约")
guests.insert(0, '令狐冲')
for person in guests:
    message = "请" + person + "参加今晚的party！"
    print(message)

# 3-6 Practice
print("找到了更大的餐桌，可以再邀请三位嘉宾")
guests.insert(0, '韦小宝')
guests.insert(2, '乔峰')
guests.append('陈家洛')
for person in guests:
    message = "请" + person + "参加今晚的party！"
    print(message)

# 3-7 Practice
print("由于新购买的餐桌无法及时送达，今天只能宴请两位嘉宾")
while len(guests) != 2:
    message = "很抱歉" + guests.pop() + ",今天无法邀请你来参加party了。"
    print(message)
for person in guests:
    print("你好，" + person +"！今天晚上依旧会邀请您参加party！")
print("今晚邀请了" + str(len(guests)) + "位嘉宾共进晚餐") # 3-9 Practice
del guests[0]
del guests[0]
print(guests)