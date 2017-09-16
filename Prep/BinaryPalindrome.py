'''
QUESTION - Find if a number has binary palindrome and count the number of set bits.
'''

num = int(input("Please enter the number: "))
binary = bin(num)[2:]
print ("\nThe number in binary is: %s" %(''.join(binary)))

if (binary == binary[::-1]):
    Length = len(binary)
    print ("\nThe inputed number is a palindrome and is of size: %s" %(Length))
else:
    print ("\nThe inputed number is not a palindrome.")
