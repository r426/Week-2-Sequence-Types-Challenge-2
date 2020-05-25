'''Week 2
Sequence Types Challenge 1

Looks for the character in every unique(!) string in the list and,
if found, counts the number of occurrences of that character
in that string and appends the string that many times to the answer list
'''

words = input("Enter a few words separated by spaces:")
print(words)
ch = input("Enter a letter:")

str_list = list(words.split(" "))
print(str_list)
print(ch)

unique_words = set(str_list)
print(unique_words)

answer_list = []
for x in unique_words:
    n = x.count(ch)
    for y in range(n):
        answer_list.append(x)
print(answer_list)
