import sys
grid = []

for s in sys.stdin:
    s = s.strip()
    if not s: break
    
    grid.append(list(s))
    

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


def find(di, dj, i, j):
    while True:
        i += di
        j += dj
        
        if i < 0 or j < 0 or i >= n or j >= m: return (-1, -1)        
        if grid[i][j] == '#': return (-1, -1)
        if grid[i][j] == '.': return i, j

    assert False
        
    
for x in moves:
    a, b = d(x)
    i, j = find(a, b, si, sj)    
    
    if i == -1: continue
    
    ii = si + a
    jj = sj + b

    grid[i][j] = grid[ii][jj]
    grid[ii][jj] = '@'
    grid[si][sj] = '.'
    
    si, sj = ii, jj


ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'O':
            ans += i * 100 + j
            
print(ans)