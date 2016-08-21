def replace(s, a, b):
    for i in s:
        print i

        if i == a:
            #print 'Y'
            #print i
            s.remove(i)
            s.insert(i, b)
    print "new list"
    for i in s:
        print s
    return s
    #else:
            #print 'N'

print replace([3, 6, 5], 6, 7)