import sys

from collections import defaultdict
from functools import cache

sys.setrecursionlimit(10 ** 6)
grid = []
for s in sys.stdin:
    s = s.strip()    
    grid.append(s)
    grid.append(s)
    grid.append(s)
    
for i in range(len(grid)):
    row = grid[i]
    nrow = []
    for x in row:
        nrow.append(x)
        nrow.append(x)
        nrow.append(x)
    grid[i] = nrow


n = len(grid)
m = len(grid[0])

seen = [[False for _ in range(m)] for __ in range(n)]
vis = [[False for _ in range(m)] for __ in range(n)]

area = set()
outer = set()

perim = 0
delta8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
delta =  [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i, j):
    global perim, start
    seen[i][j] = True
    area.add((i, j))
    
    for a, b in delta:
        ii = i + a
        jj = j + b
        if ii >= 0 and jj >= 0 and ii < n and jj < m and grid[ii][jj] == grid[i][j]:
            if seen[ii][jj] == False: dfs(ii, jj)
    return

    
ans = 0
for i in range(n):
    for j in range(m):
        if seen[i][j]: continue
        outer = set()
        area = set()
        perim = 0
        dfs(i, j)
        
        for ii, jj in area:
            for a, b in delta8:
                iii = ii + a
                jjj = jj + b
                
                if (iii, jjj) not in area:
                    outer.add((iii, jjj))
        
        corner = 0
        for ii, jj in outer:
            dirs = []
            for a, b in delta:
                iii = ii + a
                jjj = jj + b
                if (iii, jjj) in outer:
                    dirs.append((a, b))
            if len(dirs) != 2: print(ii, jj)
            assert len(dirs) == 2
            
            if dirs[0] != (dirs[1][0] * -1, dirs[1][1] * -1):
                corner += 1
        ans += corner * len(area)//9
      
print(ans)