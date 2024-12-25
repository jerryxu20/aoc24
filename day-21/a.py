import sys
import copy
from collections import deque
import string

numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [' ', '0', 'A']]
controller = [[' ', '^', 'A'], ['<', 'v', '>']]
moves = ['<', '>', '^', 'v', 'A']

def move(c):
    if c == '<': return [0, -1]
    if c == '>': return [0, 1]
    if c == '^': return  [-1, 0]
    if c == 'v': return [1, 0]
    assert False

class State:        
    def __init__(self, grid, i, j, child, target=None):
        self.child = child
        self.grid = grid
        self.pos = [i, j]

        self.n = len(grid)
        self.m = len(grid[0])
        
        self.str = []
        self.target = target
        
    def next_states(self):
        nxt = []
        for c in moves:
            node = self.copy()
            if node.child.play(c):
                nxt.append(node)
        return nxt
            
            
    def copy(self):
        return copy.deepcopy(self)
        
    def play(self, c):
        i, j = self.pos

        if c == 'A':
            if self.child:
                return self.child.play(self.grid[i][j])    
                
            if self.target[len(self.str)] != self.grid[i][j]: return False
            self.str.append(self.grid[i][j])
            return True
        
        else:
            a, b = move(c)
            i += a
            j += b     
            if i < 0 or j < 0 or i >= self.n or j >= self.m: 
                return False
            if self.grid[i][j] == ' ': 
                return False
            self.pos = [i, j]
            return True
        
    def is_goal(self):
        if self.child:
            return self.child.is_goal()
        return self.str == self.target
    
    def tostr(self):
        if self.child != None:
            return str(self.pos) + self.child.tostr()
        return str(self.pos) + "".join(self.str)
    

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

ans = 0
for s in sys.stdin:
    num = int(s.strip().strip(string.ascii_letters))
    s = list(s.strip())

    node = State(numpad, 3, 2, None, s)
    for _ in range(3):
        node = State(controller, 0, 2, node)
        
    d = bfs(node)
    ans += d * num
    
print(ans)