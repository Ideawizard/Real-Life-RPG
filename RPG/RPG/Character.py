from Dice import Dice
'''
    Every story has characters. In traditional RPGS, the characters that arent
    human (or similar to human in intelligence and mannerisms) tend to be called
    monsters. To make things simple and straightforward, I am treating monsters
    the same as if they were characters of a different race. I did not include
    race or class, however, since those characteristics are optional to the game
    I would want to make and/or the story I would want to tell. Such variables
    can be added and modified in the final iteration, and are optimal for
    interfacing.

    For the purposes of assignment, class and race will not be dictated, as most
    characters in the game will be human. Notable exceptions might be something
    like a dog or a computer. You will see in the final product :).

    - Timothy Ryan Scully

    November 8th, 2018
'''

#from here on in we will use comments like this so you can see the code more clearly

class Character(object):

    def __init__(self, name): #of course, when you make a character, the first thing you do is name him/her/whatever

        self.name = str(name)

    def HP(self, hp): #I gave characters HP, which are optional to implement as not all characters need be for combat

        self.hp = int(hp)

    def AC(self, ac): #armor class is literally the difficulty another character will have hitting them. We call it AC for short.

        self.ac = int(ac)

    def Level(self, level): #True to the RPG cannon, each character has a level of power. The programmer can delcare starting level with this method.

        self.level = int(level)

    def XP(self, xp): #Also in conjunction with the RPG standards, there level of power is proportional to their experience points.

        self.xp = int(xp)

    def Money(self, money): #I use the term "Money" instead of gold to imply that any currency can be used. Something like Gil or Clamshells or bitcoins are par for the course.

        self.money = int(money)

    def SkillCheck(self, skill, ability, DC): #I even made a method to allow auto implementation of a single skill check. It uses the d20 method.

        roll= Dice(1, 20, skill.mod + ability.mod)

        if (roll.Check(DC) == True):

            return True #It rings true if the character is successful.

        else:

            return False #Otherwise it is falseself.

            #Its worth noting that this method is optional; the check method for Dice can be implemented independently.

    def Attack(self, other, ability): #attack was a bit hard to name, since it could mean the attack value.

        roll = Dice(1, 20, self.attack + ability.mod)

        if (roll.Check(other.ac) == True): #In this case, the character is literally attacking another. Bonuses are dictated by the weapon equipped.

            self.Damage(other) #if the attack hits, damage is rolled. What that damage is can be static or a die roll. This system tries to be flexable.

            return True

        else:

            return False #Of course, failure results in nada; you deal damage only if you hit. Exceptions can be made in other functions.

    def Damage(self, other): #This method is interesting, since expecting a variable, it accepts an object.

            other.hp -= self.damage #if the object is a character with hp, damage is dealt.

    def Weapon(self, name):

            self.weapon = str(name)

class Ability(object): #This is another optional feature. In classic DnD characters have abilities that modify their rolls. Coders can invent abilities for this purpose.

    def __init__(self, name, mod): #its implemented as a seperate class, and the methods can be called on in the character class.

        self.name = name #Call it what you want

        self.mod = int(mod) #Make it what you need

class Skill(object): #Skills work the same as abilities; this more or less reflects your power level and expertise in a select skill.

    def __init__(self, name, mod):

        self.name = name #Same as above

        self.mod = int(mod) #As is below
