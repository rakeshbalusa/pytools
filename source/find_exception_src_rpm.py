import csv

licenses = []
src_rpms = []
rpm_names = []
with open('C:\\doc\\bal_rpms\\test\\exception.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if 'exception' in line[1]:
            licenses.append(line[1])
            src_rpms.append(line[2])
            rpm_names.append(line[0])
with open('C:\\doc\\bal_rpms\\test\\exception_rpms.csv', 'wb') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter = ',')
    i=0
    for i in range(len(licenses)):
        csv_writer.writerow([rpm_names[i]] + [licenses[i]] + [src_rpms[i]])
