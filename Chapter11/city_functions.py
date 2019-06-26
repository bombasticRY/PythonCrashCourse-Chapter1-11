def city_function(city, country):
    return "{}, {}".format(city.title(), country.title())

def city_function1(city, country, population):
    return "{}, {} - population {}".format(city.title(), country.title(),
                                           str(population))

def city_function3(city, country, population=""):
    if population:
        return "{}, {} - population {}".format(city.title(), country.title(),
                                           str(population))
    else:
        return "{}, {}".format(city.title(), country.title())