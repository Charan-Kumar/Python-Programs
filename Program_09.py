__author__ = 'charan'
#9. Write a program that determines whether the given number is palindrome or not

def isPalindrome(number):
    reverse_number =0
    number_copy = number
    while number > 0:
        reverse_number = reverse_number *10
        reverse_number = reverse_number + number %10
        number = number //10

    if number_copy == reverse_number:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")
