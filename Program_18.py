__author__ = 'charan'

# Merge Sort
def merge_sort(array):
    if len(array)<2:
        return
    mid = len(array)//2
    left = array[:mid]
    right= array[mid:]
    merge_sort(left)
    merge_sort(right)

    i=j=k=0
    while(i<len(left) and j <len(right)):
        if left[i] >= right[j]:
            array[k]=right[j]
            j=j+1
        else:
            array[k]=left[i]
            i=i+1
        k=k+1

    while(i < len(left)):
        array[k]=left[i]
        k=k+1
        i=i+1

    while(j < len(right)):
        array[k]=right[j]
        k=k+1
        j=j+1

