import sys
from functools import cache

arr = list(map(int, input().split()))

@cache
def f(a, iter):
    if iter == 0: return 1
    if a == 0: return f(1, iter - 1)
    n = len(str(a))
    if n % 2 == 0:
        return f(int(str(a)[0:n//2]), iter - 1) + f(int(str(a)[n//2:]), iter - 1)
    return f(a * 2024, iter - 1)

ans = 0
for x in arr:
    ans += f(x, 75)
    
    
print(ans)