String1 = input("Please enter first string: ")
String2 = input("Please enter second string: ")

String3 = set(String1).intersection(set(String2))
print(''.join(String3))
