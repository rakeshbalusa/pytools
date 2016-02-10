import json
import os

def get_json_data(location):
    with open(location, 'rb') as json_file:
        data = ''
        for line in json_file:
            data = data + line
    data = data.replace('data=', '')
    locations = []
    json_dump = json.dumps(data)
    json_data = json.loads(json_dump)
    for value in json.loads(json_data):
        locations.append(value['location'])
    fin_locs = []
    for file_loc in locations:
        try:
            file_loc = file_loc.replace('/', '\\')
            fin_locs.append(file_loc)
        except:
            pass
    return fin_locs

def get_data_json(location):
    all_files = []
    for path, subdirs, files in os.walk(location):
        for file in files:
            if file == 'data.json':
                all_files.append(os.path.join(path, file))
    return all_files



