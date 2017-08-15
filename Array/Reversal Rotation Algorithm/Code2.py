# Author - Shivam Kapoor
# This code is written in accordance of algorithm given in geeksforgeeks.
# Link - http://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

def rotate(arr, elements):
    reverse(arr, 0, elements)
    reverse(arr, elements, len(arr))
    reverse(arr, 0, len(arr))
    print (arr)

def reverse(arr, start, end):
    arr[start:end] = arr[start:end][::-1]
    print(arr)
    return arr

arr = input("Please input the array elements with spaces in between(ex - 1 2 3 ...): ").split()
elements = int(input("Please input the number of elements to be moved at a time: "))
rotate(arr, elements)
