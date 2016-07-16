import numpy as np
import random
import pylab

class Dice(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    

def rollFiveDice(sides, numDie, trails):
    dices = []
    for i in range(numDie):
        dices.append(Dice(sides))
        
    numIsSame = 0
    for i in range(trails):
        
        result = []
        for dice in dices:
            result.append(dice.roll())

        sameFlag = 1
        
        compare = result[0] 
        for j in result:
            if j == compare: continue
            elif j != compare:
                sameFlag = 0
                break
        if sameFlag:
            numIsSame += 1

    return float(numIsSame)/trails
        

print (rollFiveDice(6,5,100000))
        
