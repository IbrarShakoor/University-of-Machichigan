# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
#

count=0
avg=0

filename=input("Enter the file name:")
try:
    y=open(filename,'r')
    for words in y:
        if not words.startswith("X-DSPAM-Confidence:") :
            continue
        else:
            count = count + 1
            p=words.find("0")#Here we are finding the position of 0th
#in p we got the position now we need to convert in to float and add them normally
            #for the sum
            num=float(words[p:])#From 0th position to onwards is the float word
            avg=avg+num
    print("Count=", count)#Total no of lines
    total=avg/count
    print("Average spam confidence:",total)

except:
    print("Wrong file name")
