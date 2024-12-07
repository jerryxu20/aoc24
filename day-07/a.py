import sys
from collections import defaultdict

grid = []

ans = 0
for s in sys.stdin:
    s = s.strip()
    grid.append(s)

    a, b = s.split(":")
    
    a = int(a)
    
    arr = list(map(int, b.split()))
    
    
    n = len(arr) - 1
    for i in range(1 << n):
        sm = arr[0]
        for j in range(n):
            if i & (1 << j):
                sm += arr[j + 1]
            else:
                sm *= arr[j + 1]
            
        if (sm == a):
            ans += a
            break
            
                
print(ans)