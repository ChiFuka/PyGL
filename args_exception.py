def part(s, start, length):
    try:
        return s[start:length]
    except AssertionError:
        print 'invalid'
print part('abcde', 1, 3)
print part('', 2, 5)
