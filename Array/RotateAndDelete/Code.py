#Author - Shivam Kapoor

#Taking input
Test_Cases = int(input())
for test in range(0,Test_Cases):
    Terms = int(input())
    arr = input().split()

#Rotating array clockwise
arr1 = [None] * len(arr)
arr1[0] = arr[len(arr)-1]
for x in range(1,len(arr)):
    arr1[x] = arr[x-1]

def rotate():
    


print(arr)
print(arr1)
