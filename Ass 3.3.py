# 3.3 Write a program to prompt for a score between
# 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error
# message and exit. For the test, enter a score of 0.85.


i = float(input("Enter Score: "))


if(i<=0 and i>.9):
	print("Wrong Value")
elif(i==0.9):
	print("A")
elif(i>=0.8and i<.9):
	print("B")
elif(i>=0.7 and i<.8):
	print("C")
elif(i>=0.6 and i<.7):
    print("D")
else:
	print("F")
