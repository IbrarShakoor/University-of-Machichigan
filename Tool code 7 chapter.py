# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#



#i made the code in two ways both are correct but the solution which we need to prsent using strip fun
#so the tool will accept the first solution

filename = input("Enter the file name:")
try :
    inp=open(filename,'r')
    for words in inp:
        words=words.upper()
        words=words.rstrip()
        print(words)
except:
    print("Wrong file name")



# filename = input("Enter the file name:")
# try :
#     inp=open(filename,'r')
#     y=inp.read().upper()
#     for words in y:
#         print(words,end='')
# except:
#     print("Wrong file name")
#
