l1 = [2, 3, 4, 5, 8, 4, 3, 5, 2, 1, 8, 8, 6, 3, 4, 5, 7, 9]
str1 = "hello python three"

# Step 1. Calculate unique elements in l1.

set1 = set(l1)
uniqueL1 = len(set1)
#print("There are " + str(uniqueL1) + " unique elements in l1.")
#this line is showing error in Python Notebook.

print("There are {} unique elements in l1.".format(uniqueL1))

# Step 2. After looking at the result of Step 1, print odd elements only.

for x in set1:
    if x % 2 > 0:
        print(x)

# Step 3. For string str1 replace “three” with “3”
# and save all words in some list where all the characters should be capital.

str1 = "hello python 3"
strUpperCase = list(str1.split(" "))

# This doesn't work:
for x in strUpperCase:
    print(x)
    x = x.upper()
    print(x)
print(strUpperCase)

# This works:
for y in range(len(strUpperCase)):
    print(strUpperCase[y])
    strUpperCase[y] = strUpperCase[y].upper()
    print(strUpperCase[y])
print(strUpperCase)

#Bonus question: Explain how a tuple is immutable.

# Elements in a tuple can't be changed.
# For example, elements in strUpperCase couldn't be changed into upper case
# if strUpperCase was a tuple, a new list should be created.