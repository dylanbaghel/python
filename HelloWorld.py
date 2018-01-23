import random

name_people = ["Abhishek","Baghel","Akash","Dylan","Vikas"]
name_number = [11,22,33,44,55,66,77,88]

def randomNumber(number):
    return random.randint(1,number)

for i in range(10):
    print(name_people[randomNumber(len(name_people) - 1)],": ",name_number[randomNumber(len(name_people) - 1)])
print("\nDone")
