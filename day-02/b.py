import sys
ans = 0

def safe(arr):
    valid = 1
    inc = 0
    dec = 0
    for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) > 3 or arr[i] == arr[i - 1]:
                valid = 0

            if arr[i] > arr[i - 1]:
                inc = 1
            if arr[i] < arr[i - 1]:
                dec = 1
    if inc == 1 and dec == 1:
        valid = 0
    return valid

for s in sys.stdin:
    arr = list(map(int, s.split()))
    if safe(arr):
        ans += 1
        continue
    for i in range(len(arr)):
        narr = arr[:i] + arr[i + 1:]
        if safe(narr):
            ans += 1
            break
print(ans)