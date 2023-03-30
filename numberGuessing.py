import random


def main():
    guesses = 0
    while True:
        guesses += 1
        guess = input("Make a guess from 1 to the number you chose before: ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Guess a NUMBER")
            continue

        if guess == random_number:
            print(f"You won! You got it in {guesses} guesses")
            break
        elif guess > random_number:
            print("Guess again a lower number")
            continue
        else:
            print("Guess again a bigger number")
            continue


top_range = input("Type a random number from 1,100: ")

while True:
    if top_range.isdigit():
        top_range = int(top_range)
        break
    else:
        print("Type a number next time")
        continue


random_number = random.randint(0, top_range)


main()
