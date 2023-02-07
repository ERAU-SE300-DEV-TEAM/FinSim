# Imports
import array as arr
from dataclasses import dataclass
from FinSimController import *


#Define Player "Struct"
@dataclass
class Player:
    income : 0.0
    currentMoney: 0.0
    monthlyLosses: 0.0


# Class/ Attribute Definitions
player = Player( 0, 0, 0,)


# Function Definitions
def menu():
    startingMoneyChoice = int((input("Please select a starting money amount\n1: 1,000 \n2: 2,000 \n2: 3,000\n")))
    if startingMoneyChoice == 1:
        player.currentMoney = 1000
    if startingMoneyChoice == 2:
        player.currentMoney = 2000
    if startingMoneyChoice == 3:
        player.currentMoney = 3000

# In game this should be run every month to adjust current money according to bills/ losses
def calcCurrentMoneyMonthly():
    player.currentMoney = player.currentMoney + (player.income - player.monthlyLosses)

# In game this calcMoneyImmediate function is to adjust money on an ad hoc basis. Meant to be run for immediate payments or adjustments that are not monthly
# valueChange should be positive for increase and negative for decreases
# Argument are arbitary so as many or as little changes can be fed at once
def calcMoneyImmediate(*valueChanges):
    for num in valueChanges:
        player.currentMoney = player.currentMoney + num



# Body of Code
menu()
 # Set currentMoney, income, and monthly losses for testing
player.income = 500
player.monthlyLosses = 250
calcCurrentMoneyMonthly()
print(player.currentMoney)
calcMoneyImmediate(1000, -500)
print(player.currentMoney)
