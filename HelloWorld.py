import random

def randomNumber():
    return random.randint(1,6)

for i in range(10):
    print(randomNumber())