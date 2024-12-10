import sys

grid = []

for s in sys.stdin:
    s = s.strip()
    grid.append(list(map(int, s)))


pts = []

n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        pts.append((grid[i][j], i, j))

pts.sort()
pts = pts[::-1]

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

dp = [[set() for _ in range(m)] for _ in range(n)]

for h, i, j in pts:
    if h == 9:
        dp[i][j].add((i, j))
        continue
    
    for a, b in delta:
        ii = i + a
        jj = j + b
        if ii < 0 or jj < 0 or ii >= n or jj >= m: continue
        if grid[ii][jj] != grid[i][j] + 1: continue
        dp[i][j] = dp[i][j].union(dp[ii][jj])
        
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            ans += len(dp[i][j])
print(ans)
        
        