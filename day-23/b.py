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



arr = [x for x in nodes]

mx = []
cur = []

def backtrack(cand):
    global cur, mx
    # print(cand, cur)
    if len(cur) > len(mx):
        mx = cur.copy()
    for a in cand:
        ncand = cand.intersection(adj[a])
        rem = [x for x in ncand if x <= a]
        for x in rem:
            ncand.remove(x)
        cur.append(a)
        backtrack(ncand)
        cur.pop()
        
        
backtrack(nodes)
print(mx)

mx.sort()
print(",".join(mx))
