# n = 103
# m = 101

n = 103
m = 101


import sys

quad = [[0, 0], [0, 0]]

for s in sys.stdin:
    pos, delta = s.split()
    j, i = map(int, pos.split("=")[-1].split(","))
    dj, di = map(int, delta.split("=")[-1].split(","))
    

    i += di * 100
    j += dj * 100

    i %= n
    j %= m
    
    
    if i == n//2 or j == m//2: continue
    quad[i > n//2][j > m//2] += 1

ans = 1
for row in quad:
    for x in row:
        ans *= x
print(ans)
    

        