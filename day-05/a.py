import sys

order = []

for line in sys.stdin:
    line = line.strip()
    print("a", line)
    if line == "": break
    a, b = map(int, line.split("|"))
    order.append([a, b])
    
ans = 0
for line in sys.stdin:
    line = line.strip()
    arr = list(map(int, line.split(",")))
    mp = {}
    for i in range(len(arr)):
        mp[arr[i]] = i
        
    valid = True
    for a, b in order:
        if a not in mp or b not in mp:
            continue
        if mp[a] > mp[b]:
            valid = False
            break
    
    if valid:
        ans += arr[len(arr)//2]
        
print(ans)