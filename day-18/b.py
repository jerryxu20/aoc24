import sys
from collections import deque
N = 71
n = N
m = N

grid = [[0 for _ in range(m)] for __ in range(n)]

def valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    q = deque()
    q.appendleft((0, 0))
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
    return (n - 1, m - 1) in cost

constraints = []
for s in sys.stdin:
    a, b = map(int, s.split(','))
    constraints.append((b, a))

for i in range(len(constraints)):
    grid[constraints[i][0]][constraints[i][1]] = 1
    if not bfs():
        print(constraints[i][1], constraints[i][0])
        sys.exit()        

