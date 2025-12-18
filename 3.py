import random
try:
    r = random.randint(1, 10)
    print(r)
except AttributeError:
    print("Функції немає")
