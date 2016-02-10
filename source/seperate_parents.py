
import os
open_file = open('C:\\doc\\bal_rpms\\childs.csv', 'rb')
names = []
for line in open_file:
    line = line.strip('"')
    line = line.strip()
    names.append(line)
new_names = names
diction = {}
repeated = []
for sub_url in names:
    for new_name in new_names:
        if sub_url.startswith(new_name + '-'):
            if sub_url not in diction.keys():
                diction[sub_url] = new_name
                break
            else :
                repeated.append(sub_url + '&&&&' + new_name)
                break
        elif sub_url == new_name:
            repeated.append(sub_url + '&&&&' + new_name)
            break
not_in = []

for key, value in diction.iteritems():
    repeated.append(key + '&&&&' + value)
print len(repeated)
with open('C:\\doc\\bal_rpms\\test\\rpm_parents.csv', 'wb') as file_open:
    for sub_url in repeated:
        file_open.write(sub_url + '\n')
