import sys
from collections import defaultdict
grid = []
for s in sys.stdin:
    grid.append(list(s.strip()))
    
    
pos = defaultdict(list)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            pos[grid[i][j]].append((i, j))
            

st = set()
n = len(grid)
m = len(grid[0])
for c, arr in pos.items():
    for i, j in arr:
        for ii, jj in arr:
            if (i, j) == (ii, jj): continue
            
            di = i - ii
            dj = j - jj

            iii = i + di
            jjj = j + dj
            if iii < 0 or jjj < 0 or iii >= n or jjj >= m: continue
            st.add((iii, jjj))
print(len(st))


