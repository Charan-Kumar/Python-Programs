__author__ = 'charan'

#14. Write a c program to check given number is strong number or not.
#[ sum of factorials of digits = given number]
#Ex: 145 = 1! + 4! + 5!

def isStrong(num):
    num_copy = num
    fact_sum = 0
    while (num > 0):
        fact_sum = fact_sum + fact(num % 10)
        num = num // 10
    if fact_sum == num_copy:
        print("Strong Number")
    else:
        print("Not a Strong Number")

def fact(digit):
    if digit == 1:
        return 1
    else:
        return digit *fact(digit-1)
