import sys
from collections import deque

grid = []

def solve():
    x, y = grid[-1].split(":")[1].split(",")

    buttons = grid[:-1]
    
    
    delta = []
    for line in buttons:
        line = line.split(":")[1].split(",")
        dx = int(line[0][3:])
        dy = int(line[1][3:])
        delta.append([dx, dy])
    
    delta[0].append(3)
    delta[1].append(1)
    
    x = int(x[3:])
    y = int(y[3:])
        
    mp = {}
    mp[(0, 0)] = 0
    q = deque()
    q.append((0, 0))
    
    while q:
        a, b = q.popleft()
        if (a, b) == (x, y): return mp[(a, b)]
        for dx, dy, c in delta:
            aa = a + dx
            bb = b + dy
            
            if aa > x or bb > y: continue
            
            if (aa, bb) not in mp:
                mp[(aa, bb)] = mp[(a, b)] + c
                q.append((aa, bb))
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