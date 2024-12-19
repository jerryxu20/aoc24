import sys
from collections import deque

grid = []

def extend(arr):
    ans = []
    for c in arr:
        if c == "#":
            ans += list("##")
        if c == 'O':
            ans += list("[]")
        if c == '.':
            ans += list('..')
        if c == '@':
            ans += list("@.")
    return ans


for s in sys.stdin:
    s = s.strip()
    if not s: break
    grid.append(extend(list(s)))
    

moves = []

for s in sys.stdin:
    moves += list(s.strip())
    
n = len(grid)
m = len(grid[0])


si, sj = None, None
for i in range(n):
    for j in range(m):
        if grid[i][j] == "@":
            si, sj = i, j

def d(c):
    if c == '<': return (0, -1)
    if c == '>': return (0, 1)
    if c == '^': return (-1, 0)
    if c == 'v': return (1, 0)
    assert False


def bfs(i, j, di, dj):
    q = deque()
    q.append((i, j))

    seen = []
    seen.append((i, j))


    while q:
        i, j = q.popleft()
        
        ii = i + di
        jj = j + dj
        # not possible to push        
        if ii < 0 or jj < 0 or ii >= n or jj >= m: return False
        if grid[ii][jj] == '#': return False
        

        if grid[ii][jj] == '.': continue        
        if (ii, jj) in seen: continue
        
        q.append((ii, jj))
        seen.append((ii, jj))
        if di == 0: continue
        
        if grid[ii][jj] == ']':
            jj -= 1
        else:
            assert grid[ii][jj] == '['
            jj += 1
        
        assert ii >= 0 and jj >= 0 and ii <= n and jj <= m
        assert grid[ii][jj] not in seen
        
        q.append((ii, jj))
        seen.append((ii, jj))
        
    seen = seen[::-1]
    
    for i, j in seen:
        ii = i + di
        jj = j + dj
        
        grid[ii][jj] = grid[i][j]
        grid[i][j] = '.'
        
    return True
    
    
        
for x in moves:
    a, b = d(x)
    if bfs(si, sj, a, b):
        si += a
        sj += b
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '[':
            ans += i * 100 + j
            
print(ans)