import csv

with open('C:\\doc\\temporary\\master\\rpm-version.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if '-' + line[1] + '-' not in line[0]:
            print line[0]
