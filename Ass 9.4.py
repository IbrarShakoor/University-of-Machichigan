# 9.4 Write a program to read through the
# mbox-short.txt and figure out who has sent the greatest number of
# mail messages. The program looks for 'From ' lines and takes the
# second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the
# sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary ' \
# 'using a maximum loop to find the most prolific committer.
import collections
count=dict()
filename=input("Enter the filename:")
try:
    inp=open(filename,"r")
    for words in inp:
        if not words.startswith('From:'):
            continue
        else:
            line = words.strip().split()#here we find the each line and break into pieces
            for name in line:
                count[name]=count.get(name,0)+1#here we counted each mail how many times it's exist
    # print(count)
    del count['From:']  #We deleted the element which contain from as a key
    # print(count)#New dictionary which contain the data and number of occcurences as key/value

    bigcount = None
    bigword = None
    for word, totalcount in count.items():
        if bigcount is None or totalcount > bigcount:
            bigword = word
            bigcount = totalcount

    print(bigword, bigcount)
except:
    print("Wrong file name")

