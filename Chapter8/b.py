import a
a.say_hello()

from a import say_hello
say_hello()

from a import say_hello as hi
hi()

import a as aa
aa.say_hello()

from a import *
say_hello()