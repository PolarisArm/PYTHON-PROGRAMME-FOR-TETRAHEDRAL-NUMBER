"""
Author: Arman Hossain
Date  : 9-10-2023 (dd/mm/yy)
program for finding if a number is tetrahedral or not.
You can also find nth tetrahedral number.
"""
def tetrahedralnumber(n):
    tetrahedral = 0

    if n == 0: #check is given number is zero or not.zero is a terahedral number so we return true.
         return True
    
    if n < 0: #check if the given number is negative of not.
         return False
    
    #loop for finding if the number is tetrahedral or not.

    for i in range(1,n+1): # n+1 used instead of n beacause range function always exclude nth number
            if(int(((i*(i+2)*(i+1)))/6)) == n:
                tetrahedral = i

    if tetrahedral != 0:
        return True
    else:
        return False
    
# find tetrahedral number from 0 to 1000
for i in range(0,1000):
    a = tetrahedralnumber(i)
    if a == True:
        print(i)
# check if a given number is tetrahedral or not
print(tetrahedralnumber(25)) # It will be False.
print(tetrahedralnumber(560)) # It will be True.
     

