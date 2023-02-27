# Imports
from dataclasses import dataclass
from random import randrange

#Define Player "Struct"
@dataclass
class Player:
    turnCount: 0
    income : 0.0
    currentMoney: 0.0
    monthlyLosses: 0.0
    currentMonth: 1
    isRenting: True
    ownsCar: False
    ownsHouse: False


# Class/ Attribute Instantiations/ Declarations
player = Player(0, 0, 0, 0, 1, True, False, False)

# Function Defintions

def menu():
    startingMoneyChoice = int((input("Please select a starting money amount\n1: 1,000 \n2: 2,000 \n3: 3,000\n")))
    if startingMoneyChoice == 1:
        player.currentMoney = 1000
    if startingMoneyChoice == 2:
        player.currentMoney = 2000
    if startingMoneyChoice == 3:
        player.currentMoney = 3000

# In game this calcMoneyImmediate function is to adjust money on an ad hoc basis. Meant to be run for immediate payments or adjustments that are not monthly
# valueChange should be positive for increase and negative for decreases
# Argument are arbitary so as many or as little changes can be fed at once
def calcMoneyImmediate(*valueChanges):
    for num in valueChanges:
        player.currentMoney = player.currentMoney + num


# In game this should be run every month to adjust current money according to bills/ losses
def calcCurrentMoneyMonthly():
    player.currentMoney = player.currentMoney + (player.income - player.monthlyLosses)

def getPlayerMoney():
    print(player.currentMoney)
    return player.currentMoney

def basicMonthlyDecisionsMenu():
    n = 1
    basicDecision = -1
    while basicDecision != 0:
        print("Choose a category to allocate money towards:\n1: Food")
        if player.isRenting == True:
            n += 1
            print("%d: Rent"% n)
        if player.ownsCar == True:
            n += 1
            print("%d: Gas"% n)
        if player.ownsHouse == True:
            n += 1
            print("%d: Mortgage"% n)
        basicDecision = int(input())


def monthlyDecisions(choice):
    if choice == 1:
        expenditure = int(input("How much monet would you like to spend on rent?"))
        player.currentMoney -= expenditure



        

def randomMonthlyDecisions():
    randEvent = randrange(0,20)
    if randEvent in range (0,20):
        print("Test Event")

        

def initializeGame():
    player.turnCount = 0
    for player.turnCount in range (0,60):
        basicMonthlyDecisionsMenu()
        randomMonthlyDecisions()
        player.turnCount += 1