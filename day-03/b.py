import sys
ans = 0
const = 1
for line in sys.stdin:
    line = line.strip()
    n = len(line)
    line += '             '
    for i in range(n):
        if line[i:i + 7] == "don't()":
            const = 0
        if line[i:i + 4] == "do()":
            const = 1
        if i + 4 >= n: break
        a = 0
        b = 0
        if line[i:i + 4] != 'mul(': continue
        for j in range(i + 4, n):
            if line[j].isdigit():
                a *= 10      
                a += int(line[j])
            else:
                break
        if j == i + 4: continue
        if line[j] != ',': continue
        
        for jj in range(j + 1, n):
            if line[jj].isdigit():
                b *= 10
                b += int(line[jj])
            else:
                break
        if line[jj] != ')': continue        
        if jj == j + 1: continue
        ans += a * b * const
    
            
print(ans)