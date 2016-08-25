def file_add(f1, f2):
    file1 = open(r'd:\1.txt', 'r')
    file2 = open(r'd:\2.txt', 'r')
    content1 = file1.read()
    content2 = file2.read()

    content1 = content1 + content2
    print content1
    file1 = open(r'd:\1.txt', 'w')
    file1.write(content1)

    file1.close()
    file2.close()
    print file1
    print file2

file_add('d:\1.txt', 'd:\2.txt')