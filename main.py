# Simple Calculations Python by Jordyn
# School Work
import sys # Imports sys package
import time # Imports time package

def additionFunction(): # Simple Function for Addition
    a = int(input("Enter the first digit you wish to add: "))
    b = int(input("Enter the second digit you wish to add: "))
    addition = a + b # Adds a+b together and defines "addition" variable as the answer
    print(a, "+", b, "=", addition) # Prints a+b variables and prints the answer to console

def subtractionFunction(): # Simple Function for Subtraction
    a = int(input("Enter the first digit: "))
    b = int(input("Enter the second digit you wish to subtract: "))
    subtraction = a - b # Subtracts a+b together and defines "subtraction" variable as the answer
    print(a, "-", b, "=", subtraction) # Prints a+b variables and prints the answer to console

def multiplyFunction(): # Simple Function for Multiplying
    a = int(input("Enter the first digit: "))
    b = int(input("Enter the second digit you wish to multiply: "))
    multiply = a * b # Multiplies a+b together and defines "multiply" variable as the answer
    print(a, "x", b, "=", multiply) # Prints a+b variables and prints the answer to console

def divideFunction(): # Simple Function for Dividing
    a = int(input("Enter the first digit: "))
    b = int(input("Enter the second digit you wish to divide: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        divide = a / b # Divides a+b together and defines "divide" variable as the answer
        print(a, "/", b, "=", divide) # Prints a+b variables and prints the answer to console
    
def retryFunction(): # Function for confirmation to run another calculation
    retry = str(input("Would you like to do another calculation? (Yes/No): "))
    if retry == "Yes":
        user = True
    else:
        print("Thanks for using my simple calculation script!\nExiting Script.")
        sys.exit()

userName = input("Enter your full name: ") # User defined input
if userName == "":
    print("Type Error, No username detected")
    time.sleep(1) # Hangs/Sleeps the script for 1 second
    sys.exit() # Kills/Exit the script

user = True # Sets user to True
while user == True: # If user is equal to True run the script
    calculationType = input("Hello", userName, "Which calculation do you wish to use? (Addition/Subtraction/Multiply/Divide): ") # Prints user inputed name along with displaying calculation options
    if calculationType == "Addition":
        additionFunction()
        retryFunction() # Within the retryFunction sets user to either True to contine while loop or ends the script depending on response
    elif calculationType == "Subtraction":
        subtractionFunction()
        retryFunction()
    elif calculationType == "Multiply":
        multiplyFunction()
        retryFunction()
    elif calculationType == "Divide":
        divideFunction()
        retryFunction()
    else:
        print("No valid input entered, exiting script.")
        user = False # Invalid response setting user to False to end the loop