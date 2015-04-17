__author__ = 'charan'

#Insertion Sort

def insertion_sort(array):
    for i in range(1,len(array)):
        value = array[i]
        hole =i

        while hole>0 and value < array[hole-1]:
            array[hole]=array[hole-1]
            hole = hole -1
        array[hole] = value

