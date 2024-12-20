import sys
import math

strs = list(input().split(", "))
input()
ans = 0
for s in sys.stdin:
    s = s.strip()
    n = len(s)
    dp = [math.inf for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        if dp[i - 1] == math.inf: continue
    
        for t in strs:
            m = len(t)
            if i + m - 2 >= n: continue
            
            if s[i - 1:i-1 + m] == t:
                dp[i + m - 1] = min(dp[i + m - 1], dp[i - 1] + 1)
    if dp[-1] != math.inf:
        ans += 1
print(ans)