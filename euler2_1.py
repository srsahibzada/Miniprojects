

import sys


t = int(input().strip())

for a0 in range(t):
    try:
        n = int(input().strip())
       
    except EOFError:
        
        break
        
    #summation
    n_3 = n // 3  if (n % 3 == 0) else (n // 3) + 1
    n_5 = (n // 5) if (n % 5 == 0) else (n // 5) + 1
    n_15 = (n // 15) if (n % 15 == 0) else (n // 15) + 1 
    sum_3 = n_3/2 * ((n_3-1) * 3)
    sum_5 = n_5/2 * ((n_5-1) * 5)
    sum_15 = n_15/2 * ((n_15-1) * 15)
    print(int((sum_3 + sum_5) - sum_15))
    