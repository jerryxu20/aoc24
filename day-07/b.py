import sys
from collections import defaultdict


ans = 0
for s in sys.stdin:
    s = s.strip()

    a, b = s.split(":")
    
    a = int(a)
    
    arr = list(map(int, b.split()))
    
    
    n = len(arr)
    things = set()
    things.add(arr[0])
    
    for i in range(1, n):
        nxt = set()
        for x in things:
            nxt.add(int(str(x) + str(arr[i])))
            nxt.add(x * arr[i])
            nxt.add(x + arr[i])
        things = nxt
    if a in things:
        ans += a
                
print(ans)