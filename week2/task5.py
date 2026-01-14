n = int(input())
bukve = "ABCEHKMOPTXY"

for i in range(n):
    s = input()

    if len(s) == 6:
        if s[0] in bukve:
            if s[1].isdigit() and s[2].isdigit() and s[3].isdigit():
                if s[4] in bukve and s[5] in bukve:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
