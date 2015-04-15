__author__ = 'charan'
#8. Write a program that finds reverse of given number

def reverse_digit(number):
    reverse_number = 0
    while number > 0:
        reverse_number = reverse_number *10
        reverse_number = reverse_number + (number %10)
        number = number //10
    print("The Reverse Number is ",reverse_number)
