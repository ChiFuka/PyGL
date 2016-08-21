def dict_dist(a={}, b={}):
    print a.keys() - b.keys()

print dict_dist ({'a':'horse','b':'rope'}, {'a':'horse','b':'herb', 'c':'exception'})