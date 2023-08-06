import random

while True:
    print("(R)ock, (P)aper, (S)cissors")
    userimp = input(">")
    print("")
    userimp = userimp.lower()

    choices = ["rock", "paper", "scissors"]

    computer_rng = random.choice(choices)

    if userimp != "rock" and userimp != "paper" and userimp != "scissors" and userimp != "r" and userimp != "p" and userimp != "s":
        print("Invalid Choice!")
    else:
        break

if userimp == "r":
    userimp = "rock"
elif userimp == "p":
    userimp = "paper"
elif userimp == "s":
    userimp = "scissors"


print("Player chose: " + userimp + "\nComputer chose: " + computer_rng)


if computer_rng == userimp:
    print("Its a draw!")
elif userimp == "rock":
    if computer_rng == "scissors":
        print("Player Wins!")
    else:
        print("Computer Wins!")

elif userimp == "paper":
    if computer_rng == "rock":
        print("Player Wins!")
    else:
        print("Computer Wins!")

elif userimp == "scissors":
    if computer_rng == "paper":
        print("Player Wins!")
    else:
        print("Computer Wins!")