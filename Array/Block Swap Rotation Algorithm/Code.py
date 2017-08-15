# Author - Shivam Kapoor
# This code is written in accordance of algorithm given in geeksforgeeks.
# Link - http://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/

# Taking Inputs
arr = input("Please input the array elements with spaces in between(ex - 1 2 3 ...): ").split()
elements = int(input("Please input the number of elements to be moved at a time: "))
arrFinal = []

# Array Division
arrA = arr[0:elements]
arrB = arr[elements:len(arr)]

# Main Logic
while(len(arrA) != len(arrB)):
    if(len(arrA) < len(arrB)):
        arrBL = arrB[0:(len(arrB) - len(arrA))]
        arrBR = arrB[(len(arrB) - len(arrA)):len(arrB)]
        arrFinal = arrBR + arrBL + arrA

    if(len(arrA) > len(arrB)):
        arrAL = arrA[0:len(arrB)]
        arrAR = arrA[len(arrB):len(arrA)]
        arrFinal = arrB + arrAR + arrAL

# Printing the Array
print(arrFinal)
