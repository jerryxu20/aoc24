import sys

adj = [[] for _ in range(100)]
brute = []
for line in sys.stdin:
    line = line.strip()
    if line == "": break
    a, b = map(int, line.split("|"))
    brute.append([a, b])
    adj[a].append(b)
    
st = set()

def dfs(node):
    seen[node] = 1
    for nxt in adj[node]:
        if nxt not in st: continue
        if seen[nxt]: continue
        dfs(nxt)
    order.append(node)



def good(arr):
    mp = {}
    for i in range(len(arr)):
        mp[arr[i]] = i
    for a, b in brute:
        if a not in mp or b not in mp:
            continue
        if mp[a] > mp[b]:
            return False
    return True

ans = 0
for line in sys.stdin:
    line = line.strip()
    arr = list(map(int, line.split(",")))
    mp = {}

    if good(arr): continue

    order = []
    seen = [0 for _ in range(100)]
    st = set(arr)
    for node in st:
        if seen[node] == 0:
            dfs(node)

    order = order[::-1]    
    weight = {}
    for i, node in enumerate(order):
        weight[node] = i

    arr2 = sorted(arr, key=lambda x: weight[x])
    ans += arr2[len(arr2)//2]
    
print(ans)