import random

def numberGenerator(amount, min, max):
    luvut = ""
    for i in range(amount):
        luvut += str(random.randint(min, max))
    return luvut

print(numberGenerator(3, 0, 9))
print(numberGenerator(4, 3, 6))