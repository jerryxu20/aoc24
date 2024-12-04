import sys
grid = [s.strip() for s in sys.stdin]


n = len(grid)
m = len(grid[0])

ans = 0

def valid(cube):
    a = cube[0][0] + cube[1][1] + cube[2][2]
    b = cube[2][0] + cube[1][1] + cube[0][2]
    cnt = 0
    if a == "MAS" or a == "SAM":
        cnt += 1
    if b == "MAS" or b == "SAM":
        cnt += 1
    return cnt == 2

for i in range(n):
    for j in range(m):
        if i + 3 <= n and j + 3 <= m:
            cube = []
            for ii in range(i, i + 3):
                cube.append(grid[ii][j:j+3])
            if valid(cube):
                ans += 1
                
print(ans)