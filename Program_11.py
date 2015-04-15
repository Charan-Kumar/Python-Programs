__author__ = 'charan'

#11. Write a program that determines whether the given number is febonacci number or not

def isFiboNum(num):
    if num == 1 or num == 0:
        print("Fibo Number")
        return
    a=0
    b=1
    c=0
    flag = 0
    while(c < num):
        c = a+b
        if c == num:
            flag =1
            break
        a=b
        b=c

    if flag:
        print("Fibo Number")

    else:
        print("Not Fibo Number")
