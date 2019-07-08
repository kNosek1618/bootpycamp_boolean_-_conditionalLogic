
from random import randint
num = randint(1,1000)

#two ways for the same equals
if num % 2 == 0:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")


if num % 2 != 0:
    print(str(num) + " is odd")
else:
    print(str(num) + " is even")
