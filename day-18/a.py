import sys
from collections import deque
N = 71
n = N
m = N

t = 0
grid = [[0 for _ in range(m)] for __ in range(n)]

for s in sys.stdin:
    a, b = map(int, s.split(','))
    t += 1 
    if t < 1024:
        grid[b][a] = 1


q = deque()
q.appendleft((0, 0))

def valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cost = {}
cost[(0, 0)] = 0
while q:
    i, j = q.popleft()
    
    for a, b in delta:
        ii = i + a
        jj = j + b
        if not valid(ii, jj): continue
        if grid[ii][jj] == 1: continue
        if (ii, jj) not in cost:
            cost[(ii, jj)] = cost[(i, j)] + 1
            q.append((ii, jj))
print(cost[(n - 1, m - 1)])