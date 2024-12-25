import sys
import copy
from collections import deque, defaultdict
import string
import math
from functools import cache

numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [' ', '0', 'A']]
controller = [[' ', '^', 'A'], ['<', 'v', '>']]
moves = ['<', '>', '^', 'v', 'A']

NUMPAD_PATHS = {}
CONTROLLER_PATHS = {}

def move(c):
    if c == '<': return [0, -1]
    if c == '>': return [0, 1]
    if c == '^': return  [-1, 0]
    if c == 'v': return [1, 0]
    assert False


def bfs(s):
    q = deque()
    q.append(s)
    seen = set()

    ans = 0
    while q:
        z = len(q)
        for _ in range(z):
            state = q.popleft()
            for nxt in state.next_states():
                if nxt.tostr() in seen: continue
                seen.add(nxt.tostr())
                q.append(nxt)        
                
                if nxt.is_goal(): return ans + 1
        ans += 1
    return None

path = []
paths = defaultdict(list)
vis = set()
def dfs(i, j, grid):
    paths[grid[i][j]].append(path.copy())
    vis.add((i, j))
    for c in moves:
        if c != 'A':
            a, b = move(c)
            ii = i + a
            jj = j + b
            if ii < 0 or jj < 0 or ii >= len(grid) or jj >= len(grid[0]): continue
            if grid[ii][jj] == ' ': continue 
            if (ii, jj) not in vis:
                path.append(c)
                dfs(ii, jj, grid)
                path.pop()
                
    vis.remove((i, j))

for i in range(len(numpad)):
    for j in range(len(numpad[0])):
        paths = defaultdict(list)
        vis = set()
        dfs(i, j,  numpad)
        NUMPAD_PATHS[numpad[i][j]] = copy.deepcopy(paths)

for i in range(len(controller)):
    for j in range(len(controller[0])):
        paths = defaultdict(list)
        vis = set()
        dfs(i, j, controller)
        CONTROLLER_PATHS[controller[i][j]] = copy.deepcopy(paths)



def ff(seq, layer):
    seq = ['A'] + seq
    ans = 0
    for i in range(1, len(seq)):
        ans += f(seq[i - 1], seq[i], layer)
    return ans

@cache
def f(a, b, layer):
    ans = math.inf
    if layer == 26: return 1
    if layer == 0:
        for path in NUMPAD_PATHS[a][b]:
            ans = min(ans, ff(path + ['A'], layer + 1))
    else:
        for path in CONTROLLER_PATHS[a][b]:
            ans = min(ans, ff(path + ['A'], layer + 1))
    return ans

ans = 0
for s in sys.stdin:
    num = int(s.strip().strip(string.ascii_letters))
    s = list(s.strip())
    cost = ff(s, 0)
    ans += cost * num
print(ans)