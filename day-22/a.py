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
    for _ in range(2000):
        x = f(x)
    ans += x
print(ans)