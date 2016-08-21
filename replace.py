def myreplace(s, a, b):
    pos = s.find(a)
    l = len(a)
    print pos
    print l
    posb = 0
    #for i in range(pos, (pos+l)):
    #    s[pos] = b[posb]
    #    posb = posb +1
     #   pos = pos +1
    s2 = s[0:pos] + b + s[(pos+l):]
    print s
    print s2
    return s2

print myreplace('ffffiiiff', 'ii', 'aa')