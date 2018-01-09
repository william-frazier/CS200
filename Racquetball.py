#William Frazier
#CS200
#HW08

import random

def racquet(games):
    """
    Simulates games of racquetball to determine who wins.
    Input "games" picks the amount of games to be simulated and will print out
    total number of wins and the probability of winning. This assumes a 60% chance
    of winning while serving and a 50% of winning while opponent serves.
    """
    
    wins = 0
    for i in range(games):
        myScore = 0
        opScore = 0
        server = 1
        while ((myScore != 21) and (opScore != 21)):
            scorer = random.randint(1,10)
            if server == 1:
                #60% chance 
                if scorer <= 6:
                    myScore += 1
                else:
                    #change server
                    server = 0
            else:
                #50% chance
                if scorer <= 5:
                    server = 1
                else:
                    #change server
                    opScore += 1
        if myScore == 21:
            wins += 1
    print("I won", wins, "out of", games, "games. \nProbability of me winning =", wins/games)
    
"""
I won 8243 out of 10000 games. 
Probability of me winning = 0.8243
"""