import sys
from collections import defaultdict
import math
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
        st.add((i, j))
        for ii, jj in arr:
            if (i, j) == (ii, jj): continue
            
            di = i - ii
            dj = j - jj

            if di == 0:
                dj = dj//abs(dj)
            if dj == 0:
                di = di//abs(di)
            if di != 0 and dj != 0:
                g = math.gcd(abs(di), abs(dj))
                di //= g
                dj //= g
                
            iii = i
            jjj = j
            while True:
                iii += di
                jjj += dj
                
                if iii < 0 or jjj < 0 or iii >= n or jjj >= m: break
                st.add((iii, jjj))                
print(len(st))



