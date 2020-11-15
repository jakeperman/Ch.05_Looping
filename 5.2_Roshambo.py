'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
# Sets up variables for tracking
go = True
options = ["Rock", "Paper", "Scissors"]
userwins = 0
cpuwins = 0
while go is True:
    inp = int(input("\033[33mPlease Select Rock(0), Paper(1), Scissors(2), or Quit(3)"))
    # checks if user correctly selected one of the 3 options
    if inp in range(3):
        cpuchoice = random.randint(0, 2)
        if inp == cpuchoice:
            print("\033[95mYou picked:\033[37m", options[inp] + "\033[95m. Cpu also picked:\033[37m", options[cpuchoice] + "\033[95m. It's a tie")
            continue
        else:
            # this loop determines the winner by comparing all possibilities
            for i in range(3):
                if inp == i:
                    # Compares the difference of opposing choices against a calculated set (1, 1, -2) of win conditions
                    if inp-cpuchoice in [1, 1, -2]:
                        print("\033[95mYou picked:\033[37m", options[inp] + "\033[95m. Cpu picked:\033[37m", options[cpuchoice] + "\033[95m. You Win!")
                        userwins += 1
                    else:
                        print("\033[95mYou picked:\033[37m", options[inp] + "\033[95m. Cpu Picked:\033[37m", options[cpuchoice] + "\033[95m. You Lose!")
                        cpuwins += 1
                else:
                    continue
        print("\033[33mCurrent Score -- \033[95mYou:\033[37m", userwins, "\033[95mCpu:\033[37m", cpuwins)
    elif inp == 3:
        print("Bye!")
        break
    else:
        print("\033[91mNot a valid option\n")
        continue















