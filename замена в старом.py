def replace(s, a, b):
    for i in range(0, len(s)):
        if s[i] == a:
            s[i] =b
    return s

lst = [3,6,5]
print replace(lst, 3, 7)