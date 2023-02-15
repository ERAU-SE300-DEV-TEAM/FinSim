# Imports
from dataclasses import dataclass

#Define Player "Struct"
@dataclass
class Player:
    income : 0.0
    currentMoney: 0.0
    monthlyLosses: 0.0
    currentMonth: 1


# Class/ Attribute Instantiations/ Declarations
player = Player( 0, 0, 0, 1)


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
