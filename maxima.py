def maxima(n):
    z = list()
    for i in str(n):
        z.append(int(i))
    print sorted(z, reverse=True)

maxima(124)