__author__ = 'charan'

# Bubble Sort

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp=array[j+1]
                array[j+1]=array[j]
                array[j]=temp
    print(array)

bubble_sort([1,2,0,0,0,0,1,1,2,3,4,5])
