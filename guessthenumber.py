import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("enter the number:"))
    if user == number:
        print("hurray!")
        print(f" u guessed the correct number , the number is {number}")
        break
    else:
        print(f" u guessed the wrong number , the number is {number}")
        