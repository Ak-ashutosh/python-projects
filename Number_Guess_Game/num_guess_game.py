# Number Guessing Game
import random

ran_number = random.choice(range(1, 100))

counter = 1
while True:
    userNum = int(input('Enter Number : '))
    counter += 1

    if userNum == ran_number:
        print(f'Correct Number {userNum}')
        print(f'Total Count Attempts are {counter}')
        break
    elif userNum > ran_number:
        print(f"It's Too High {userNum}")
    elif userNum < ran_number:
        print(f"It's Too Low {userNum}")
    else:
        print(f'Invalid input {userNum}')
        break
