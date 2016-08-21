def avg(a, b, *c):
    i = 0
    s = 0
    for x in c:
        s= s +x
        i = i + 1
    a = (s +a + b)/(i + 2)
    lst = [a]+[b]+[c]
    return a

print avg(5,2,4,5,6)