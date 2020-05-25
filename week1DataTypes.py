'''Task A
Write a Python program to display the current date and time.
'''
import datetime
import math

currentDateTime = datetime.datetime.now()
print(currentDateTime)

'''Task B
Write a Python program which accepts
the radius of a circle from the user
and compute the area.
'''

radius = float(input("Enter the radius:"))
print("The area is: " + str(math.pi*radius*radius))

'''Task C
Write a Python program which accepts
a sequence of comm-separated numbers from the user
and generates a list and a tuple with those numbers
'''

myString = input("Enter a few numbers separated by \",\":")
myList = list(myString.split(","))
myTuple = tuple(myString.split(","))
print(myList)
print(myTuple)

'''Task D
Write a Python program to test whether
a number is within 100 of 1000 or 2000
(between 900 and 1100 or between 1900 and 2100 inclusive)
'''

theNumber = int(input("Enter an integer number:"))
if(theNumber >= 900 and theNumber <= 1100) or (theNumber >= 1900 and theNumber <= 2100):
    print("Yes!")
else:
    print("No...")

'''Task E
Write a Python program to check whether
a specified value is contained in a group of values
'''

myValues = [1,5,8,3]
yourNumber = int(input("Enter an integer number between 1 and 10:"))

if yourNumber in myValues:
    print("Yes! Your number is in my values!")
else:
    print("No... You didn't guess...")

'''Task F
Write a Python program to get the difference
between a given number and 17.
If the number is greater than 17,
return double of absolute difference.
'''

yourFinalNumber = int(input("Enter an integer number between 1 and 35:"))
if yourFinalNumber <= 17:
    print(yourFinalNumber-17)
else:
    print(abs(yourFinalNumber-17)*2)
