# n = 103
# m = 101

n = 103
m = 101


import sys

quad = [[0, 0], [0, 0]]

pts = []
dir = []


for s in sys.stdin:
    pos, delta = s.split()
    j, i = map(int, pos.split("=")[-1].split(","))
    dj, di = map(int, delta.split("=")[-1].split(","))
    
    pts.append((i, j))
    dir.append((di, dj))


class UF:
    def __init__(self, n):
        self.id = [x for x in range(n)]
        
    def join(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        
        self.id[a] = b
        return True
    
    def find(self, a):
        if self.id[a] != a: 
            self.id[a] = self.find(self.id[a])
        return self.id[a]

def id(i, j):
    return j + i * m

d4 = [(0, -1), (0, 1), (1, 0), (-1, 0)]
ans = None
res = None


for t in range(100000):
    picture = [[0 for _ in range(m)] for __ in range(n)]
    for p, d in zip(pts, dir):
        i = p[0] + d[0] * t
        i %= n
        
        j = p[1] + d[1] * t
        j %= m
        
        picture[i][j] = 1
    
    comps = len(pts)
    uf = UF(n * m)
    
    for i in range(n):
        for j in range(m):
            if picture[i][j] != 1: continue
            for a, b in d4:
                ii = i + a
                jj = j + b
                if ii < 0 or jj < 0 or ii >= n or jj >= m or picture[ii][jj] != 1: continue
                if uf.join(id(i, j), id(ii, jj)):
                    comps -= 1
    
    if comps < 250:
        ans = t
        res = picture
        break
    
        
print(ans)
        