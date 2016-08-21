def Exclude(lst1=[], lst2=[]):
    for i in range(0, len(lst1)):
        if lst1[i] in lst2:
            lst1.remove(i)
    print(lst1)
    return lst1

Exclude([1,2,3], [3,4,5])

def Exclude(lst1, lst2):
    i =0
    while i < len(lst1):

        if lst1[i] in lst2:
            del(lst1[i])
        else:
            i +=1
    return lst1
    print(lst1)

Exclude([1,2,3], [3,4,5])
