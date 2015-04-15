__author__ = 'charan'

#13. Write a program that takes one number & one digit as input,
# and finds the number of times the digit occurs in the given number

def digit_count(num,digit):
    count=0
    while(num > 0):
        if num %10 == digit:
            count = count+1
        num = num // 10

    print("Count is ", count)

