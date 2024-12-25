import sys
val = {}
nodes = set()
for line in sys.stdin:
    line = line.strip()
    if not line: break
    
    lit, v = line.split(": ")
    val[lit] = int(v)
    nodes.add(lit)

dep = {}   
    
for line in sys.stdin:
    line = line.strip()
    a, op, b, _, c = line.split()
    dep[c] = (a, b, op)

    
    nodes.add(a)
    nodes.add(b)
    nodes.add(c)

def f(a, b, op):
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'XOR':
        return a ^ b
    assert False

def dfs(node):
    if node in val:
        return val[node]

    a, b, op = dep[node]
    val[node] = f(dfs(a), dfs(b), op)
    return val[node]
    
    
ans = 0
for node in nodes:
    if node[0] == 'z':
        idx = int(node[1:])
        v = dfs(node)
        ans |= v << idx
print(ans)