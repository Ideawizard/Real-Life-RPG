from Dice import Dice
from Character import *

"""
    There are always three things you need for a good Role Playing Game, be it
over table with friends or on the computer by yourself. One are some rules, which
the computer provides almost by default. The other is Player Characters, which are
of course provided by the player class. The last this is a GameMaster, or GM.
The classes below fill the core functions of the GM..

"""

class Campaign(object): #Fist of course is to lay out the campaign.It is the world the player plays in

    def __init__(self, name): #initalize with an official name

        self.name = str(name)

    def Genre(self, name): # I originally added genre, as a way of choosing and switching genres. May not be used in final product.

        self.genre = name

class Location(object): # could easily be a class in and of itself. Might make it so with further developments. UPDATE: Followed your recommendations and it is now a class :).

    def __init__(self, name, description, A, B, C, D): #initialized with everything you expect.

        self.name = str(name) #Gotta call it something.

        self.description  = str(description) #This is literally what the player reads when they "enter" the location. I originally had a method where you print it, but that belongs on the "outside".

        self.optionA = A #I gave the player 4 options by default. Would not have minded making this aspect more modular, but I'm kinda swamped so here we go...

        self.optionB = B

        self.optionC = C

        self.optionD = D

        self.selected = "" #we initialize a variable selected as an empty string

    def Menu(self): #We print out a menu this way. Makes it easier.

        print(self.description)

        print ("\n\nOPTION A: ",self.optionA,"\nOPTION B: ",self.optionB,"\nOPTION C: ",self.optionC,"\nOPTION D: ",self.optionD) #We print the different options so the player knows what to do.

        self.Select() # and allow the player to select their option, of course.

    def Select(self):

        selection = input("\nType the letter of your Selection: ") #What almost every DM or GM asks their players when its their turn to act. UPDATE: remade it so the instructions are more clear.

        if (selection == "A" or selection == "a"): #All made to work with lower or uppercase character. Might be an easier way to type this.

            self.selected = self.optionA

        elif (selection == "B" or selection == "b"):

            self.selected = self.optionB

        elif (selection == "C" or selection == "c"):

            self.selected = self.optionC

        elif (selection == "D" or selection == "d"):

            self.selected = self.optionD

        else:

            print ("That is not a valid option. Select A,B,C,or D. No spaces. Lower case letters should work as well.") # considering throwing an exception instead, but this will work for now.

            self.Select()

    def Results(self, results): # this is more for when you get results but you don't change location. Loops back to where you were.

        print ("\n",results,"\n")

        self.Menu()


class Item(object): #It's not a good RPG unless you can collect some swag.

    def __init__(self, name):#like everythign else in existance, it gets a name upon discovery.

        self.name = str(name)

    def Taken(self, owner): #Whan happens when the main character takes this object?

        self.owner = owner

        self.equipped = False

    def Equip(self): #What happens when you use/wear/arm yourself with said item

        if (self.equipped != None and self.equipped == False):

            self.equipped = True

            if (self.equipped == True): #check if equipped. Might need to reimplement. should work when the player equipps and unequipps the weapon.

                if(self.type == "weapon"):

                    self.owner.attack = self.attack #add the weapons attack bonus

                    self.owner.damage = self.damage #and damage bonus

                    self.owner.Weapon(self.name)

                if (self.type == "armor"):

                    self.owner.ac += self.ac

        self.equipped = True #a little redundant, but necessary if equipped isn't specified

    def Unequip(self): #gotta unarm it sometimes.

        if(self.equipped != None and self.equipped == True):

            self.equipped = False

            if (self.type == "weapon"): #Was originally in the 'Weapon' function, but it makes more sense here.

                self.owner.attack = 0

                self.owner.damage = 0

            if (self.type == "armor"):

                self.owner.ac -= self.ac

    def Weapon(self, attack, damage): #Declare it as a weapon.

        self.type = "weapon" #set the type

        self.attack = int(attack)

        self.damage = int(damage)


    def Armor(self, ac):

        self.type = "armor" #similar problems as with the weapon function. Might need to reimplement

        self.ac = ac


class Reward(object): #The reason you came to the table and the thing that allows this to all become one giant hamster wheel...

    def __init__(self, name, recipient): #You name the reward and designate a character as the recipient. Can easily be a monster as well :).

        self.name = str(name)

        self.recipient = recipient

    def Money(self, money): #It's nice to get paid for your hard work.

        recipient = self.recipient

        recipient.money += money

    def XP(self, xp): #It's also nice to gain xp points.

        recipient = self.recipient

        recipient.xp += int(xp)

    def LevelUp(self, xp): #and uh... what happens when you get enough xp?

        recipient = self.recipient #I find myself writing this repetitively. Is there a way to scope or replicate this better?

        if (recipient.xp >= xp):

            recipient.level += 1 #Player 1 has gained a level.

            return True

        else:

            return False #or has he?


#Further Notes; Would be nice to have a GUI or Gameloop class as well to make this a proper game. Might develop more in the future outside of class.
