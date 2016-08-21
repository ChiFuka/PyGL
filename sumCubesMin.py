def sumCubes(a,b,c):
    min1 = 0
    min2 = 0
    for i in (a,b,c):
        if a<=b:
            min1 = a
            if b<c:
                min2 = b
            else:
                min2 = c
        elif b<=a:
            min1 = b
            if c<a:
                min2 = c
            else:
                min2 = a
        elif c<=a:
            min1 =c
            if b<a:
                min2 = b
            else:
                min2 = a
    return min1,min2
print sumCubes(3,3,3)