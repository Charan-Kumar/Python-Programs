__author__ = 'charan'
#15. Write a program that determines whether the given two numbers are amicable or not
#[Two numbers are amicable if each one of them is equal to the sum of proper divisors of others.
#Ex: 220 and 284 are amicable numbers. Proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,110.
#The sum of these divisors is 284. The proper divisors of 284 are 1,2,4,71,142. The sum of these divisors is 220.]

def isAmicables(num1,num2):
    num1_divisors_sum = 0
    num2_divisors_sum = 0

    for i in range(1,num1):
        if num1 % i == 0:
            num1_divisors_sum = num1_divisors_sum + i

    for i in range(1,num2):
        if num2 % i == 0:
            num2_divisors_sum = num2_divisors_sum + i


    if(num1_divisors_sum == num2 and num2_divisors_sum == num1):
        print("Both are Amicable")
    else:
        print("Not Amicable")

