#Author - Shivam Kapoor

Test_Cases = int(input())
for test in range(0,Test_Cases):
    Terms = int(input())
    arr = input().split()
    elements = int(input())

    #Logic in 1 line xD
    arr = [arr[(i+elements) % len(arr)] for i in range(0, len(arr))]

    print (" ".join(arr))
