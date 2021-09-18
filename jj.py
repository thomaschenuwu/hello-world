import random
from random import random

result = ""

Player = 0
PlayerWins = 0

ComputerInput = ""
ComputerWins = 0

while ComputerWins < 2 and PlayerWins < 2:
    PlayerInput = str(input("Input your choice: "))
    PlayerInput = PlayerInput.lower()
    Computer = int(random()*3) + 1
    if Computer == 1:
        ComputerInput = "rock"
    if Computer == 2:
        ComputerInput = "paper"
    if Computer == 3:
        ComputerInput = "scissors"

    if "rock" in PlayerInput:
        Player = 1
        if Computer == 1:
            result = "tied"
        if Computer == 2:
            result = "lost"
        if Computer == 3:
            result = "won"
    if "paper" in PlayerInput:
        Player = 2
        if Computer == 1:
            result = "won"
        if Computer == 2:
            result = "tied"
        if Computer == 3:
            result = "lost"
    if "scissors" in PlayerInput:
        Player = 3
        if Computer == 1:
            result = "lost"
        if Computer == 2:
            result = "won"
        if Computer == 3:
            result = "tied"

    print("You went " + PlayerInput + ". Computer went " + ComputerInput + ".")
    print("You " + result)

    if result == "lost":
        PlayerWins = PlayerWins + 1
    if result == "lost":
        ComputerWins = ComputerWins + 1

    print(str(PlayerWins) + " : " + str(ComputerWins))

if ComputerWins == 2:
    print("You suck")
if PlayerWins == 2:
    print("you are bad")


    
