import sys
from collections import defaultdict
adj = defaultdict(set)

nodes = set()
for s in sys.stdin:
    a, b = s.strip().split("-")
    adj[a].add(b)
    adj[b].add(a)
    nodes.add(a)
    nodes.add(b)
    
ans = 0
for a in nodes:
    for b in adj[a]:
        s = adj[a].intersection(adj[b])
        for c in s:
            if 't' in a[0] + b[0] + c[0]:
                ans += 1
print(ans//6)