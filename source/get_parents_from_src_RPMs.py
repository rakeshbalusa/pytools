import csv
parents = []
with open('C:\\doc\\temporary\\master\\src_RPMs.csv', 'rb') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')
    for line in csv_read:
        try:
            parents.append([line[0],line[1],line[2],line[2][0:line[2].index('-' + line[1])]])
        except:
            parents.append([line[0], line[1], line[2], 'no parent found'])
with open('C:\\doc\\temporary\\master\\parents.csv', 'wb') as csv_file:
    csv_write = csv.writer(csv_file, delimiter=',')
    csv_write.writerows(parents)
