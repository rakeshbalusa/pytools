#
#  Copyright (c) 2015 nexB Inc. and others. All rights reserved.
#


import csv
import requests

'''
'input_file' consists of a column named 'URL to Original Code' which has the URLs
to be validated. These URLs must be in the format 'http://.....'
'''


def check_urls(input_file, output_file):
    url_list = []
    with open(input_file, 'rb') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        next(csv_reader)  # skip header
        for row in csv_reader:
            url_list.append(row['URL to Original Code'])
    output = []
    with open(output_file, 'wb') as csv_file:
        csv_write = csv.writer(csv_file, delimiter=',')
        csv_write.writerow(['Working URLs'])  # header
        for url in url_list:
            try:
                r = requests.head(url, auth=('user', 'pass'))
                if r.status_code not in [404, 500, 501, 502, 503, 504, 405, 408, 410]:
                    csv_write.writerow([url])
            except:
                pass

if __name__ == '__main__':
    import sys
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    check_urls(input_file, output_file)
