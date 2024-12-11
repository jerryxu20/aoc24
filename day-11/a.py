import sys


arr = list(map(int, input().split()))

def f(a):
    ans = []
    for x in a:
        if x == 0:
            ans.append(1)
        elif len(str(x)) % 2 == 0:
            n = len(str(x))
            ans.append(int(str(x)[0:n//2]))
            ans.append(int(str(x)[n//2:]))
        else:
            ans.append(x * 2024)
    return ans


for _ in range(75):
    arr = f(arr)
    # print(arr)
    
print(len(arr))
