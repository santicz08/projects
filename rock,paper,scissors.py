import random


def play():
    user = input("Choose: Rock(r) Paper(p) Scissor(s): ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return("Its a draw!")
    elif win(user, computer):
        return("You won!!")
    else:
        return ("You lost!!")

def win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())