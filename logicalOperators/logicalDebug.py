
import random

'''
This function checks who won in a rock paper scissor game, between a human
and the cpu.

The computer makes a random choice(1 through 3).

The function compares choice(the users choice) to cpuChoice(the computers
choice) and prints who wins or if it is a draw.
'''
def checkWhoWins(choice):
    '''
    cpuChoice is a number 1-3, the number corresponds to an answer:
    1 = rock
    2 = scissors
    3 = paper
    '''
    cpuChoice = random.randint(1,3)
    
    # This condition checks if there is a draw
    if((choice == 'rock' and cpuChoice == 1) or (choice == 'scissors' and cpuChoice == 2)
        or (choice == 'paper' and cpuChoice == 3)):
        print("DRAW!")
    
    # This condition checks if the human wins
    elif((choice == 'rock' and cpuChoice == 2) or (choice == 'scissors' and cpuChoice == 3)
        or (choice == 'paper' and cpuChoice == 1)):
        print("HUMAN WINS!")
    
    # This condition checks if the cpu wins
    elif((choice == 'rock' or cpuChoice == 3) or (choice == 'scissors' or cpuChoice == 1)
        or (choice == 'paper' and cpuChoice == 2)):
        print("CPU WINS!")
    
    return

checkWhoWins("rock")
checkWhoWins("paper")
checkWhoWins("scissors")