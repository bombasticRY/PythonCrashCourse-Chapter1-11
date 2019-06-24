# 8-3 Practice
def make_shirt(size, word):
    print("\nThis shirt's size is " + size + " and word is " + word)

make_shirt('medium', 'Go Go Go')
make_shirt(size='large', word='Die Die Die')

# 8-4 Practice
def make_shirt(size='large', word='I love Python!'):
    print("\nThis shirt's size is " + size + " and word is " + word)

make_shirt()
make_shirt('medium')
make_shirt('small', 'FXCK!')

# 8-5 Practice
def describe_city(name, country='china'):
    print(name.title() + " is in " + country.title())

describe_city('beijing')
describe_city(name='tianjin')
describe_city('reykjavik', 'iceland')