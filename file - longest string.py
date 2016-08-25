def longest_string():
    file = open(r'd:\3.txt', 'r')
    string = ''
    for line in file:
        print line
        if len(string) < len(line):
            string = line
    file.close()
    return string

print longest_string()