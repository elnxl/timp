import sys
import os

filename = 'names.txt'
s3cr3t_filename = '../never/ever/open/this/folder/prog_limits.ini'

if not os.path.exists(filename):
    f = open(filename, 'w+')
    f.close()
with open (s3cr3t_filename, 'r+') as l, open(filename, 'r+') as d:
    limit = int(l.readline())
    current = int(l.readline())
    if current < limit:
        name = str(input('Enter your Full name: '))
        data = d.read()
        if name in data.splitlines():
            print('Your name: %s is already entered in the list' %name)
        else:
            d.write(name + '\n')
            print('Your name: %s is added to the list' %name)
        current += 1
        l.seek(len(str(limit))+1)
        l.write(str(current))
        print('Your program usage limit is %d, your current usage is %d' % (limit,current))
    else:
        print ('Your trial period is over, please buy full version or delete the program')
        sys.exit(0)