a = input().strip()
b = input().strip()

m = len(b)
bb = b + b

shifts = set()
for i in range(m):
    shifts.add(bb[i:i+m])

count = 0
for i in range(len(a) - m + 1):
    if a[i:i+m] in shifts:
        count += 1

print(count)
