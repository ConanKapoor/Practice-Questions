# Author - Shivam Kapoor
# This code is written as minimal as possible.

# Rotating array clockwise and performing deletion.
def rotate(arr):
    count = 1
    while (len(arr) > 1):
        arr = [arr[(i+1) % len(arr)] for i in range(0, len(arr))]
        arr.pop(len(arr)-count) if len(arr)>count else arr.pop()
        count+=1
    arr1.append(arr[0])

# Taking input
arr1 = []
Test_Cases = int(input())
for test in range(0,Test_Cases):
    Terms = int(input())
    arr = input().split()
    rotate(arr)

print ("\n".join(arr1))
