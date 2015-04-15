__author__ = 'charan'
#12. Write a c program to check given number is Armstrong number or not.

def isArmStrong(num):
    num_copy = num
    sum = 0
    while num > 0:
        digit = num %10
        sum = sum + (digit * digit *digit)
        num = num // 10

    if num_copy == sum:
        print("Arm Strong Number")
    else:
        print("Not a Arm Strong Number")
