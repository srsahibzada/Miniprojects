#hackerrank 

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    #naive solution
    mult_3 = [x for x in range(0,n) if x % 3 == 0]
    mult_5 = [x for x in range(0,n) if x % 5 == 0 and x % 3 != 0]
    print(sum(mult_3) + sum(mult_5))