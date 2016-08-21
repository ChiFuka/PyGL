def anagram(w1, w2):
    answer = 0
    for i in w2:
        #print i
        #print w1.count(i)
        #print w2.count(i)
        if w1.count(i)== w2.count(i):
            answer += 1
    if answer == len(w2):
        return True
    else:
        return False

print anagram('silent', 'listen')
print "Feee"
print anagram('kasatka', 'kassa')
