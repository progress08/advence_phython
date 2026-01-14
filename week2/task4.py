n, m = map(int, input().split())
s = input().strip()

words = set()
for i in range(n - m + 1):
    words.add(s[i:i+m])

print(len(words))
