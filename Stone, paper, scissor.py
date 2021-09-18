import random as rd
# Rock paper Scissor

print("Rules of this Game:-\n"
      "1. Rock vs Scissor = Rock win, Rock vs Paper = Rock loose\n"
      "2. Paper vs Scissor = Paper loose, Paper vs Rock = Paper win\n"
      "3. Scissor vd Rock = Scissor loose, Scissor vs Paper = Scissor win")
rando = rd.randint(1, 3)
if rando == 1:
    comp = "r"
elif rando == 2:
    comp = "p"
elif rando == 3:
    comp = "s"


def game(computer, player):
    if computer == player:
        return print("The game is ends with a Tie")
    elif computer == "r":
        if player == "p":
            return True
        elif player == "s":
            return False
        else:
            print("Error! please choose from the given options\n"
                  "Rock (r), Paper (p) and Scissor (s)")
    elif computer == "p":
        if player == "s":
            return True
        elif player == "r":
            return False
        else:
            print("Error! please choose from the given options\n"
                  "Rock (r), Paper (p) and Scissor (s)")
    elif computer == "s":
        if player == "r":
            return True
        elif player == "p":
            return False
        else:
            print("Error! please choose from the given options\n"
                  "Rock (r), Paper (p) and Scissor (s)")


print("Computer choose :- Rock (r), Paper (p) and Scissor (s)")
you = input("Player choose :- Rock (r), Paper (p) and Scissor (s):- \n").lower()
a = game(comp, you)

if a is True:
    print("Player wins")
elif a is False:
    print("Computer wins player loose")

print(F"Computer choose:- {comp}")
print(F"Player choose:- {you}")
