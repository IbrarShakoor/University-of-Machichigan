
filename = input("Enter the file name:")
try :
    inp=open(filename,'r')
    # y=inp.read().upper()
    for words in inp:
        words=words.upper()
        words=words.rstrip()
        print(words)
except:
    print("Wrong file name")