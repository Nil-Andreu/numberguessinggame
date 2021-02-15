import random

random_num = random.randint(1,10)

user = int(input("What number do you think it is?"))

while random_num != user:
    if random_num > user:
        print("Your number is lower")

    elif random_num < user:
        print("Your number is lower")

    user = int(input("Type your number again"))

print("You have the correct number")