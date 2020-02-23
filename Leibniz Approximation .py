# Put your code here
import math 
value = int(input("Enter the number of iterations: "))

pi = math.pi
count = 0
x = 0
z = 1
y = 1


for count in range(value -1):
    count += 1

    if count % y == 0:
        x = count * 2 + 1
        denom = 1/x
        z = z - denom
        y = y + 2
    else:
        x = count * 2 + 1
        denom = 1/x
        z = z + denom


    
    print(x, denom, z)
    
totalValue = z * 4
print(totalValue)
        


