
s = input()

for x in range(10):
    a = s[0]
    b = s[2]
    c = s[4]

    if a == 'x':
        a = x
    else:
        a = int(a)

    if b == 'x':
        b = x
    else:
        b = int(b)

    if c == 'x':
        c = x
    else:
        c = int(c)

    if s[1] == '+':
        if a + b == c:
            print(x)
    if s[1] == '-':
        if a - b == c:
            print(x)

