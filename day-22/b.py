import sys
import collections
MOD = 16777216
def f(x):
    x ^= x * 64
    x %= MOD
    x ^= x // 32
    x %= MOD
    x ^= x * 2048
    x %= MOD
    return x


    
ans = 0
sm = collections.defaultdict(int)
for a in sys.stdin:
    x = int(a.strip())
    delta = []
    for _ in range(2000):
        nx = f(x)
        delta.append((nx % 10) - (x % 10))
        x = nx

    cur = int(a.strip()) % 10
    seen = set()
    for i in range(len(delta)):
        cur += delta[i]
        if i >= 3:
            state = tuple(delta[i-3:i+1])
            if state not in seen:
                seen.add(state)
                sm[state] += cur
                

ans = 0
for a, b in sm.items():
    ans = max(ans, b)
print(ans)