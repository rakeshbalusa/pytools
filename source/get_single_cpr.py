import csv
cpy_dict = {}
def remove_duplicates_list(input):
    empty = []
    for value in input:
        if value not in empty:
            empty.append(value)
    return empty
with open('C:\\doc\\bal_rpms\\test\\all_cprs.csv', 'rb') as read:
    read_file = csv.reader(read, delimiter=',')
    resource = []
    copys = []
    for line in read_file:
        resource.append(line[0])
        copys.append(line[1])
        cpy_dict[line[0]] = []
    print len(resource)
    print len(copys)
    for i in range(len(copys)):
        lis = cpy_dict[resource[i]]
        lis.append(copys[i])
        cpy_dict[resource[i]] = lis
final_dict = {}
for key, value in cpy_dict.iteritems():
    temp = cpy_dict[key]
    temp = remove_duplicates_list(temp)
    final_dict[key] = temp
row = ''
output = {}
for key, value in final_dict.iteritems():
    row = '\n'.join(value)
    output[key] = row
with open('C:\\doc\\bal_rpms\\test\\sing_cprs.csv', 'wb') as write:
    write_csv = csv.writer(write, delimiter=',')
    write_csv.writerows(zip(output.keys(), output.values()))
