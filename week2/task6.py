def all_eq(lst):
    mx = 0
    for s in lst:
        if len(s) > mx:
            mx = len(s)

    res = []
    for s in lst:
        while len(s) < mx:
            s = s + "_"
        res.append(s)

    return res
