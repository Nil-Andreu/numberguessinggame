import random

random_num = random.randint(1,10)

user = int(input("What number do you think it is?"))

number_tries = 1

while random_num != user:
    if number_tries == 3:
        break
    number_tries =+ 1
    
    if random_num > user:
        print("Your number is lower")

    elif random_num < user:
        print("Your number is lower")

    user = int(input("Type your number again"))

print("You have the correct number")
