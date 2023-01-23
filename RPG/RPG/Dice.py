from random import randint
#TIMOTHY RYAN SCULLY

# You can't play an RPG without dice, and the closest thing to dice on a computer are random number generators. This class uses the ladder for the former.

class Dice(object):

    # We start by initializing the important details; how many dice are you rolling, how many sides do they have, and what you add or subtract to the result.
    def __init__(self, number, sides, mod):

        self.number = int(number)

        self.sides = int(sides)

        self.mod = int(mod)

    #And of course, we roll the dice to get the results. This is where the magic happens.
    def roll(self):

        roll = 0

        for i in range(0,self.number):

            roll += randint(1, self.sides) + self.mod

        return int(roll)

    #As a bonus, I added a little feature that lets you compare the results of a roll to an arbitrary number.
    #It returns true when you succeed, and Flase when you do not.
    #This streamlines the process of checking for success. It can be used for anything, and will be implemented by other Classes.
    def Check(self, DC):

        roll = int(self.roll())

        if (roll >= int(DC)):
            return True
        elif (roll < int(DC)):
            return False
