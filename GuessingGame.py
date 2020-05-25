import random
from math import floor

print("Choose an integer between 0 and 100 inclusive.\nI'll guess it! Click \"y\" when ready.")
enter = input()

Iguessed = False
numberOfGuesses = 0
fromNumber = 0
toNumber = 100
while(Iguessed == False):
    myGuess = floor(random.uniform(fromNumber, toNumber + 1))
    numberOfGuesses += 1
    print("It's " + str(myGuess) + ", right?")
    yourNumber = input("y – if Yes!\n+ – if your number is bigger\n- – if your number is smaller.")
    if yourNumber == "+":
        fromNumber = myGuess + 1
    elif yourNumber == "-":
        toNumber = myGuess - 1
    else:
        Iguessed = True
print("Your number is " + str(myGuess) + "! I made " + str(numberOfGuesses) + " guesses.")
