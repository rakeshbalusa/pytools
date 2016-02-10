
output=[]
with open('C:\\doc\\temporary\\master\\licenses.csv', 'rb') as loc:
    for line in loc:
        line = line.strip()
        if 'gpl 3.0 or later' in line.lower():
            output.append(line + ',' + 'yes')
        elif 'gplv3+' in line.lower():
            output.append(line + ',' + 'yes')
        elif 'gpl 3.0' in line.lower():
            output.append(line + ',' + 'yes')
        elif 'lgpl 3.0' in line.lower():
            output.append(line + ',' + 'yes')
        elif 'lgpl 3.0 or later' in line.lower():
            output.append(line + ',' + 'yes')
        elif 'lgplv3+' in line.lower():
            output.append(line + ',' + 'yes')
        elif 'gplv3' in line.lower():
            output.append(line + ',' + 'yes')
        elif 'lgplv3' in line.lower():
            output.append(line + ',' + 'yes')
        else:
            output.append(line)
with open('C:\\doc\\temporary\\master\\category.csv', 'wb') as write:
    for line in output:
        write.write(line + '\n')
