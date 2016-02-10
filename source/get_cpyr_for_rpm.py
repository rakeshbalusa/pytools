import csv

def remove_duplicates_list(input):
    empty = []
    for value in input:
        if value not in empty:
            empty.append(value)
    return empty

# only_cpys.csv consists of two columns the first column has the resource and the second column has the copyright present in that resource
# the third columns

rpm_list = []
cpy_dict = {}
with open('C:\\doc\\scope_v2\\cpys\\cprs.csv', 'rb') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=',')
    for row in file_reader:
        cpy_dict[row[0]] = row[1]
        rpm_list.append(row[2])
# rpm-list consists of a single column with the list of all the RPMs in the resources in only_cpys.csv


# with open('C:\\doc\\scope_v2\\caspian\\copys\\rpm-list.csv', 'rb') as rpms:
#     for line in rpms:
#         line = line.strip()
#         rpm_list.append(line)
new_rpm_list = []
for val in rpm_list:
    if val:
        new_rpm_list.append(val)
rpm_list = []
rpm_list = new_rpm_list


print len(rpm_list)
rpm_cpy_dict = {}
for rpm in rpm_list:
    rpm_cpy_dict[rpm] = []
for rpm in rpm_list:
    for key, value in cpy_dict.iteritems():
        if rpm in key:
            temp = rpm_cpy_dict[rpm]
            temp.append(value)
            rpm_cpy_dict[rpm] = temp
for key, value in rpm_cpy_dict.iteritems():
    row = '\n'.join(list(set(value)))
    rpm_cpy_dict[key] = row
with open('C:\\doc\\scope_v2\\cpys\\final_cprs.csv', 'wb') as write:
    write_csv = csv.writer(write, delimiter=',')
    write_csv.writerows(zip(rpm_cpy_dict.keys(), rpm_cpy_dict.values()))
print len(rpm_cpy_dict.keys())
print len(rpm_cpy_dict.values())
