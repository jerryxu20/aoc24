import sys

from collections import defaultdict
from functools import cache

sys.setrecursionlimit(10 ** 6)

grid = []
for s in sys.stdin:
    s = s.strip()
    grid.append(s)
    

n = len(grid)
m = len(grid[0])

seen = [[False for _ in range(m)] for __ in range(n)]

st = set()
area = set()
perim = 0
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(i, j):
    global perim
    seen[i][j] = True
    area.add((i, j))
    for a, b in delta:
        ii = i + a
        jj = j + b
        
        if ii >= 0 and jj >= 0 and ii < n and jj < m and grid[ii][jj] == grid[i][j]:
            if seen[ii][jj] == False:
                dfs(ii, jj)
        else:
            perim += 1
    return

ans = 0
for i in range(n):
    for j in range(m):
        if seen[i][j]: continue
        area = set()
        perim = 0
        dfs(i, j)
        ans += perim * len(area)
print(ans)