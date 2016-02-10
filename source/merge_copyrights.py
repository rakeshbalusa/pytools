import os
import csv

def merge_cpyrts(location):
    rsc = []
    copys = []
    with open(location, 'rb') as loc:
        reader = csv.reader(loc)
        for row in reader:
            rsc.append(row[0])
            copys.append(row[1])
    for i in range(len(rsc)):
        try:
            rsc[i] = rsc[i][0:rsc[i].index('-extract/')]
        except:
            pass
    cpy_dict = {}
    for each in rsc:
        cpy_dict[each] = ''
    for i in range(len(rsc)):
        cpy_dict[rsc[i]] = cpy_dict[rsc[i]] + '\n' + copys[i]
    with open('C:\\doc\\temporary\\test\\output.csv', 'wb') as write:
        wr = csv.writer(write, delimiter=',')
        for key, value in cpy_dict.iteritems():
            wr.writerow([key, value])
    print len(cpy_dict.keys())
loc = 'C:\\doc\\temporary\\test\\all_copyrights.csv'
merge_cpyrts(loc)
