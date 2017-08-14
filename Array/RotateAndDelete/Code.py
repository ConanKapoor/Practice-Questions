#Author - Shivam Kapoor

#Taking input
Test_Cases = int(input())
for test in range(0,Test_Cases):
    Terms = int(input())
    arr = input().split()

#Rotating array clockwise and performing deletion.
count = 1
while (len(arr) > 1):
    arr = [arr[(i+1) % len(arr)] for i in range(0, len(arr))]
    arr.pop(count-1) if len(arr)>count else arr.pop(len(arr)-1)
    count+=1

#Priting result
print(arr)
