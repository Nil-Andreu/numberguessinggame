import random

num = random.randint(1,10)

user = int(input("What number do you think it is?"))

number_tries = 3

status = ('correct' if user >= 0 and user <= 10 else 'not correct')

if status == 'correct':
    while num != user:
        if number_tries == 3:
            break
        
        number_tries =+ 1

        if num > user:
            print("Your number is lower")

        elif num < user:
            print("Your number is lower")

        user = int(input("Type your number again"))

    print("You have the correct number")

else:
    print("Your number is not allowed")
