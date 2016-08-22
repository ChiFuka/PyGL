def dict_dist(a={}, b={}):

    cnt = 0
    if len(a.keys())== len(b.keys()):
        for k in a:
            if a[k] != b[k]:
                cnt+=1
    elif len(a.keys()) < len(b.keys()):
        for k in a:
            if a[k] != b[k]:
                cnt+=1
        cnt = cnt + (len(b.keys()) - len(a.keys()))
    elif len(a.keys()) > len(b.keys()):
        for k in b:
            if b[k] != a[k]:
                cnt+=1
        cnt = cnt + (len(a.keys()) - len(b.keys()))
    return cnt


print dict_dist ({'a':'horse','b':'rope', 'c':'exception'}, {'a':'hrrse'})