# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:

count=0
fopen=open('oy.txt','r')
for line in fopen:
    if not line.startswith('From:'):#Not started by from keywords so skip
        continue
    else:
        words=line.strip().split()
        print(words[1])  #Jo print krwana ha wo krwa lo index dy k
        count=count+1


print("There were", count, "lines in the file with From as the first word")
