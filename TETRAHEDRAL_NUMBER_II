"""
Tetrahedral number is sum of nth triangular number. SUM((N*(N+1))/2)
"""

import time

def find_tetrahedral_number(n):
    if n == 0:
        return True  
    elif n < 0:
        return False  
    else:
        tetrahedral_number = 0
        i = 1
        while tetrahedral_number < n:
            tetrahedral_number += i * (i + 1) // 2
            i += 1
        return tetrahedral_number == n
    
#Loop for finding tetrahedral number from 0 to 100000-1
n = 1000000
t0 = time.time()
for i in range(n):
    if find_tetrahedral_number(i):
        print(i, "True")
t1 = time.time()

print("Time required: " + str(t1-t0) )
