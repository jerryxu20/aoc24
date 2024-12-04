import sys
grid = [s.strip() for s in sys.stdin]


n = len(grid)
m = len(grid[0])

ans = 0

delta = [[0, 1],[0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
for i in range(n):
    for j in range(m):
        for a, b in delta:
            s = ""
            ii = i
            jj = j
            for _ in range(4):
                if ii < n and ii >= 0 and jj < m and jj >= 0:
                    s += grid[ii][jj]
                ii += a
                jj += b
            if s == "XMAS":
                ans += 1
print(ans)