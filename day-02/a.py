import sys
ans = 0

for s in sys.stdin:
    arr = list(map(int, s.split()))
    inc = 0
    dec = 0
    valid = 1
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) > 3 or arr[i] == arr[i - 1]:
            valid = 0
        
        if arr[i] > arr[i - 1]:
            inc = 1
        if arr[i] < arr[i - 1]:
            dec = 1
    if inc == 1 and dec == 1:
        valid = 0
    if valid:
        ans += 1        

print(ans)