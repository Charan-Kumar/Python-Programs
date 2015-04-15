__author__ = 'charan'
#4. Write a program to find largest of 3 numbers

def large_among_three(num1,num2,num3):
    if num1 > num2 :
        if num1 > num3:
            print("The Large One is",num1)
        else:
            print("The Large One is",num3)

    else:
        if num2 > num3:
            print("The Large One is",num2)
        else:
            print("The Large One is",num3)
