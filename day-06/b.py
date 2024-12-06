import sys
from collections import defaultdict
grid = []
for s in sys.stdin:
    grid.append(list(s.strip()))
n = len(grid)
m = len(grid[0])

ans = 0
def rot(i, j):
    i, j = j, i
    j *= -1
    return (i, j)


def stuck():
    a = -1
    b = 0
    st = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '#' and grid[i][j] != '.':
                while True:
                    if (i, j, a, b) in st: return True
                    st.add((i, j, a, b))
                    cnt = 0
                    while cnt < 4:
                        ii = i + a
                        jj = j + b
                        if ii < 0 or jj < 0 or ii >= n or jj >= m:
                            return False
                            
                        if grid[ii][jj] == '#':
                            a, b = rot(a, b)
                            cnt += 1
                            continue
                        else: 
                            i = ii
                            j = jj
                            break
                    
                    if cnt == 4: return True
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            grid[i][j] = '#'
            if stuck():
                ans += 1
            grid[i][j] = '.'
print(ans)