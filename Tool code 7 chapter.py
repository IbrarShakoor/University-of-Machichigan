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
