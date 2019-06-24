# 8-6 Practice
def city_country(name, country):
    print(name.title() + ", " + country.title())

city_country('beijing', 'china')
city_country('wuha', 'china')
city_country('paris', 'french')

# 8-7 Practice
def make_album(singer_name, album_name, song_num=""):
    album = {'singer': singer_name, 'album': album_name,}
    if song_num:
        album['songs'] = song_num
    return album

print(make_album('s1', 'a1'))
print(make_album('s2', 'a3', 20))

# 8-8 Practice
while True:
    singer = input("please input singer's name: ")
    if singer == 'q':
        break
    album = input("please input album's name: ")

    if album == 'q':
        break

    make_one_album = make_album(singer, album)
    print(make_one_album)