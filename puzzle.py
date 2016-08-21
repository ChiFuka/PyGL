def puzzle(a, b):
    answer = 0
    for i in b:
        print i
        print a.count(i)
        print b.count(i)
        if a.count(i) >= b.count(i):
            answer += 1
    if answer >= len(b):
        return True
    else:
        return False

print puzzle('kasatka', 'taksa')
print "Feee"
print puzzle('kasatka', 'kassa')
