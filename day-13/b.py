import sys
from collections import deque

grid = []

def solve():
    x, y = grid[-1].split(":")[1].split(",")
     
    x = int(x[3:]) + 10000000000000
    y = int(y[3:]) + 10000000000000
    buttons = grid[:-1]
    
    delta = []
    for line in buttons:
        line = line.split(":")[1].split(",")
        dx = int(line[0][3:])
        dy = int(line[1][3:])
        delta.append([dx, dy])
    

    x1, y1 = delta[0]
    x2, y2 = delta[1]
    m = (y - (y1 * x)/x1) / (y2 - y1 * x2/x1)
    n = (x - x2 * m)/x1
    
    m = int(round(m))
    n = int(round(n))
    
    N = [n - 2, n - 1, n, n + 1, n + 2]
    M = [m - 2, m - 1, m, m + 1, m + 2]
    
    for nn in N:
        for mm in M:
            if x == nn * x1 + mm * x2 and y == nn * y1 + mm * y2: return 3 * nn + mm
    return 0



ans = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        ans += solve()
        grid = []
    else:
        grid.append(line)
ans += solve()

print(ans)