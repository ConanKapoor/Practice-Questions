# Author - Shivam Kapoor
# This code is written as minimal as possible.
import math

# Taking inputs.
dimension = int(input("Please Enter the number of rows/columns: "))

# Initializing the matrix.
Matrix = [[0 for x in range(dimension)] for y in range(dimension)]

# Taking inputs in matrix.
for i in range(dimension):
    for j in range(dimension):
        if (dimension < 4):
            Matrix[i][j] = int(input("Please input Matrix items: "))
        else:
            Matrix[i][j] = i+j

#Printing entered matrix
print('\nThe inputed matrix looks like - \n')
print('\n'.join([''.join(['{:3}'.format(item) for item in row])for row in Matrix]))
print('\n')

# Logic starts -
for i in range(0,math.ceil(dimension/2)):
    for j in range(i,dimension-i-1):
        temp = Matrix[i][j]
        Matrix[i][j] = Matrix[j][dimension-i-1]
        Matrix[j][dimension-i-1] = Matrix[dimension-i-1][dimension-j-1]
        Matrix[dimension-i-1][dimension-j-1] = Matrix[dimension-j-1][i]
        Matrix[dimension-j-1][i] = temp

#Printing rotated matrix
print('\nThe newly rotated matrix looks like - \n')
print('\n'.join([''.join(['{:3}'.format(item) for item in row])for row in Matrix]))
print('\n')

'''
Just For Idea -
1 2 3     1  2  3  4  [0][0] -> [rows-1][0]
4 5 6     5  6  7  8  [0][1] -> [rows-2][1]
7 8 9     9  10 11 12 [0][2] -> [rows-3][2]
          13 14 15 16 [0][4] -> [rows-4][3]

3 6 9     4  8  12 16
2 5 8     3  7  11 15
1 4 7     2  6  10 14
          1  5  9  13
'''
