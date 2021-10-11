

try:
    f = open('sample2.txt', 'r')

    #aa = f.read()
    rows = f.readlines()

    print(f.read())


    # for row in rows:
    #     print(row.strip())
    f.close()
    # for row in f.readline():
    #     print(row)

except IOError:
    print('Could not open/read file')

lines_to_write = ['Hello worlds\n', 'I have an internship interview tomorrow\n', 'wish me luck\n']

try:
    file_to_write = open('sample2.txt', 'w')
    file_to_write.writelines(lines_to_write)
    file_to_write.close()
except IOError:
    print('Cannot write the file!')

