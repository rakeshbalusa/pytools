import csv

def get_arch(location):
    with open(location,'rb') as loc:
        reader = csv.reader(loc)
        arch = []
        for row in reader:
            if 'unable to find :' in row[0]:
                arch.append('NA')
            elif '.i686.' in row[0]:
                arch.append('i686')
            elif '.x86_64.' in row[0]:
                arch.append('x86_64')
            elif '.noarch.' in row[0]:
                arch.append('noarch')
            elif '.src.' in row[0]:
                arch.append('src')
            else:
                arch.append('no arch found')
    print len(arch)
    with open('C:\\doc\\bal_rpms\\test\\archs.csv', 'wb') as write:
        for line in arch:
            write.write(line + '\n')

get_arch('C:\\doc\\bal_rpms\\test\\rpms.csv')
