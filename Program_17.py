__author__ = 'charan'

#17.Write a program to binary search


#Iterative Way

def binary_search(ary,x):
    left = 0
    right = len(ary)-1
    while(left <= right):
        mid = (left+right)//2
        if ary[mid] == x:
            return mid
        elif ary[mid] < x:
            left = mid +1
        elif ary[mid] > x:
            right = mid - 1
    return -1

#Recursive Way
def binary_search_recursive(ary,x,left,right):
    if right < left:
        print("Not Found");
        return
    else:
        mid = (left+right)//2
        if ary[mid] == x:
            print(mid)
            return
        elif x > ary[mid]:
            binary_search_recursive(ary,x,mid+1,right)
        elif x < ary[mid]:
            binary_search_recursive(ary,x,left,mid-1)
