s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    a = [0] * 26

    for ch in s1:
        a[ord(ch) - ord('A')] += 1

    for ch in s2:
        a[ord(ch) - ord('A')] -= 1

    ok = True
    for x in a:
        if x != 0:
            ok = False

    if ok:
        print("YES")
    else:
        print("NO")
