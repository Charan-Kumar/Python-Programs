__author__ = 'charan'
#10. Write a program that finds n-th febonacci term

def nth_febonacci(n):
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    print("Nth Fibo ",c)
