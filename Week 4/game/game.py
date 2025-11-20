import random
import sys

def main():

    numero = random_number()

    while True:
        try:
            chute = int(input("Guess: "))

            if chute == numero:
                sys.exit("Just right!")

            elif chute > numero:
                print("Too large!")
                continue

            elif chute < numero and chute >= 0:
                print("Too small!")
                continue

            else:
                continue

        except (ValueError):
            continue

#function to get a valid number
def random_number():
    while True:
        try:
            random_number = int(input("Level: "))
            level = random.randint(1, random_number)
            break
        except (ValueError):
            continue
    return level

main()
