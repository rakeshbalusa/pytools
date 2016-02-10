#
#  Copyright (c) 2015 nexB Inc. and others. All rights reserved.
#

import csv

def create_hierarchies(rpm_file_names, output_file_name):
    rpm_names = []
    with open(rpm_file_names, 'rb') as file:
        for line in file:
            line = line.rstrip()
            rpm_names.append(line)
    parent_component = {}
    for list_1_rpm in rpm_names:
        list_1_rpm = list_1_rpm.rstrip()
        for list_2_rpm in rpm_names:
            list_2_rpm = list_2_rpm.rstrip()
            if list_2_rpm.startswith(list_1_rpm + '-'):
                parent_component[list_2_rpm] = list_1_rpm
            elif list_1_rpm == list_2_rpm:
                if list_1_rpm not in parent_component.keys():
                    parent_component[list_2_rpm] = list_1_rpm
    write_dict_to_csv(output_file_name, parent_component)
    
def write_dict_to_csv(output_file_name,parent_component):
    with open(output_file_name, 'wb') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',')
        file_writer.writerows([['child', 'parent']])
        for key, value in parent_component.items():
            file_writer.writerow([key, value])
if __name__ == '__main__':
    import sys
    rpm_file_names = sys.argv[1]
    output_file_name = sys.argv[2]
    create_hierarchies(rpm_file_names, output_file_name)
