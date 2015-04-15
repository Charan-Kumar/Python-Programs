__author__ = 'charan'
#13. Write a c program to check given number is perfect number or not.
#[Perfect number - Sum of proper divisors (divisors < n) is given number. In other words, sum of divisors= 2*n]
#Ex:  6 is a perfect number
#6  = 1 + 2 + 3

def isPerfect(num):
    divisible_sum = 0
    for i in range(1,num):
        if (num % i == 0):
            divisible_sum = divisible_sum + i
    if divisible_sum == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
