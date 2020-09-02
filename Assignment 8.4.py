# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split()
# method. The program should build a list of words.
# For each word on each line check to see if the word is already in
# the list and if not append it to the list. When the program completes, sort and
# print the resulting words in alphabetical order.

#
# fopen=open("romeo.txt",'r')
# lst = list()                       # list for the desired output
# for line in fopen:                    # to read every line of file romeo.txt
#     word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
#     for element in word:           # check every element in word
#         if element in lst:         # if element is repeated
#             continue               # do nothing
#         else :                     # else if element is not in the list
#             lst.append(element)    # append
# lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
# print(lst)





fopen=open("romeo.txt",'r')
lst = list()
for line in fopen:
    word= line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else :
            lst.append(element)
lst.sort()
print(lst)


string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome an'
print(string.strip('an'))