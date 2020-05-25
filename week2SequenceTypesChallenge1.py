'''Week 2
Sequence Types Challenge 1

Looks for the character in every string in the list and,
if founds, counts the number of occurrences of that character
in that string and appends the string that many times to the answer list
'''

words = input("Enter a few words separated by spaces:")
print(words)
ch = input("Enter a letter:")

str_list = list(words.split(" "))
print(str_list)
print(ch)

answer_list = []
for x in str_list:
    index = x.find(ch)
    if index >= 0:
        n = x.count(ch)
        for y in range(n):
            answer_list.append(x)
print(answer_list)
