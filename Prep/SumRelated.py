'''
QUESTION - Calculate the sum of two integers and if the number of digits in sum
           equal to one of the integer then return sum else return n.
'''
Integer1 = int(input("Please enter 1st integer: "))
Integer2 = int(input("Please enter 2nd integer: "))

Sum = Integer1 + Integer2
Length = [int(x) for x in str(Sum)]

if (len(Length) == Integer1 or len(Length) == Integer2):
    print ("\nSum: %s" %(Sum))
else:
    print("\nNumber of digits: %s" %(len(Length)))
