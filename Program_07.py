__author__ = 'charan'
#14. Write a program to find sum of digits of given number up to single digit [lucky digit]

def single_digit_sum(num):
    while True:
        sum = digit_sum(num)
        if sum < 9:
            break
        num = sum
    print("Single Digit Sum", sum)

def digit_sum(num):
    sum=0
    while(num > 0):
        sum = sum + num%10
        num = num // 10
    return sum

