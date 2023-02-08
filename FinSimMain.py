# Imports
import array as arr
from FinSimController import *


# Function Definitions
def menu():
    startingMoneyChoice = int((input("Please select a starting money amount\n1: 1,000 \n2: 2,000 \n3: 3,000\n")))
    if startingMoneyChoice == 1:
        player.currentMoney = 1000
    if startingMoneyChoice == 2:
        player.currentMoney = 2000
    if startingMoneyChoice == 3:
        player.currentMoney = 3000


# Function Calls
menu()

