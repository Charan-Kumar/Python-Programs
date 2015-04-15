__author__ = 'charan'

#5. Write a program that counts the number of digits in the given number

def digit_count(num):
    count = 0
    while(num>0):
        count = count+1
        num = num//10
    print("Count is ",count)

