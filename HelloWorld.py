import random

name_people = ["Abhishek","Baghel","Akash","Dylan","Vikas"]

def randomNumber():
    return random.randint(1,len(name_people) - 1)

for i in range(10):
    print(name_people[randomNumber()])