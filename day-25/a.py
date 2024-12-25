import sys
import copy
from collections import deque
import string

grid = []

keys = []
locks = []
for s in sys.stdin:
    s = s.strip()
    if len(s) == 0:
        if grid[0].count('#') == len(grid[0]):
            keys.append(grid)
        else:
            locks.append(grid)
        grid = []
        continue
    grid.append(s)
    
if grid[0].count('#') == len(grid[0]):
    keys.append(grid)
else:
    locks.append(grid)
n = len(grid)
m = len(grid[0])

ans = 0
for lock in locks:
    for key in keys:
        bad = False
        for i in range(n):
            for j in range(m):
                if lock[i][j] == '#' and key[i][j] == '#':
                    bad = True    
        if not bad:
            ans += 1
print(ans)