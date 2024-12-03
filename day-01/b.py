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

for a in l:
    ans += a * r.count(a)
print(ans)
    