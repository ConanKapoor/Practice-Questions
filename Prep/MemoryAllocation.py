array = [1,3,8,11,3]
total = 0

for x in array:
    total = total + x

power = 1
while(power):
    if(total <= (2**power)):
        print (2**power)
        break
    else:
        power = power + 1
