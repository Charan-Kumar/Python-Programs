__author__ = 'charan'

#Quick Sort

def partition(start,end,array):
    pivot = array[end]
    index = 0
    for i in range(0,end):
        if array[i] <= pivot:
            temp = array[index]
            array[index]=array[i]
            array[i]=temp
            index = index+1
    temp = array[end]
    array[end]=array[index]
    array[index]=temp
    return index

arr=[7,2,1,6,8,5,3,4]
def quick_sort(start,end,arr):
    if(start < end):
        pivot_index = partition(start,end,arr)
        quick_sort(0,pivot_index-1,arr)
        quick_sort(pivot_index+1,end,arr)

quick_sort(0,7,arr)
print(arr)