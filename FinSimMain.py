# Imports
import array as arr
from FinSimController import *

# Class/ Attribute Definitions
menuChoice = arr.array("i")

# Function Definitions
def menu():
    menuChoice.append(int(input("Select the amount of starting money:\n1: 1,000 USD \n2: 1,500 USD \n3: 2,000 USD\n")))
    print(menuChoice)

# Body of Code
menu()
controllerMain(menuChoice)
