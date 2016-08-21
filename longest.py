def longest(t):
    t1 = t.split(' ')
    tmp = t1[0]
    for i in t1:
        if len(tmp) < len(i):
            tmp = i
    return tmp

print (longest('s dd ffff'))