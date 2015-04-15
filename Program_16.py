__author__ = 'charan'

#16.Write a program to convert decimal number to binary

def toBinary(decimal):
    if decimal == 0:
        return
    else:
        reminder = decimal%2
        toBinary(decimal//2)
        print(reminder,end="")
