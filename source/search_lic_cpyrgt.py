file_names = []
copyrights = []


with open('C:\\doc\\temporary\\file_copy.csv', 'rb') as files:
    for line in files:
        line = line.strip()
        line = line.strip('"')
        file_names.append(line)
with open('C:\\doc\\temporary\\copys.csv', 'rb') as files:
    for line in files:
        line = line.strip()
        line = line.strip('"')
        copyrights.append(line)
print len(file_names)
print len(copyrights)

def check_copyright(file, copyright):
    with open(file, 'rb') as file_reader:
        lines = ''
        for line in file_reader:
            lines = lines + line
        if lines.find(copyright) >= 0:
            print 'found ' + copyright + 'in file : ' + file
            return 1
        else:
            print 'not found '+copyright+'in file : '+file
            return 0

i = 0
for file in file_names:
    check_copyright(file, copyrights[i])
    i=i+1
