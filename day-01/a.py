import sys
l = []
r = []
for s in sys.stdin:
    a, b = map(int, s.split())
    l.append(a)
    r.append(b)
    
l.sort()
r.sort()

ans = 0
for a, b in zip(l, r):
    ans += abs(a - b)
print(ans)