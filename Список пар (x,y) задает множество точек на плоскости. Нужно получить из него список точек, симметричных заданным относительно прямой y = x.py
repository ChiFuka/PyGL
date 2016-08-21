
xs = [(1,2),(3,4),(5,6)]
sx = []
for (y,s) in xs:
    sx.append((s, y))
print sx

sx = [(y,s) for (s,y) in xs]
print sx

for x in range(len(xs)):
    (a,b ) = xs[x]
    xs[x] = (b, a)
    print xs