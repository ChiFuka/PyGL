def isInList(e, lst):
    i = 0
    count = 0
    for i in lst:
        if i == e:
            count = count + 1
    return count


print isInList(13, [6, 2, 3, 4, 6])
