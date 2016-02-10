import json
import requests
import tempfile

def download(uri):
    """
    Fetch the file at uri, saving it to a temp file and return the path to
    this temp file.
    """
    print uri
    response = requests.get(uri)

    status = response.status_code
    if status != 200:
        raise Exception('download: Download failed for %(uri)r '
                        'with %(status)r' % locals())

    tmp = tempfile.NamedTemporaryFile(mode='wb',
                                      prefix='npm-minecode-fetched-file',
                                      suffix='.json',
                                      delete=False)
    file_name = tmp.sub_url
    try:
        tmp.write(response.content)
    finally:
        tmp.close()
    return file_name

def get_npm_names(location):
    with open(location, 'rb') as json_file:
       json_data_dict = json.load(json_file)
#   removing the '_updated' key which has the time of update
    json_data_dict.pop('_updated')
    all_package_metadata_json = []
    for key, value in json_data_dict.iteritems():
        all_package_metadata_json.append('https://skimdb.npmjs.com/registry/' + value.get('sub_url'))
    for json_url in all_package_metadata_json:
        try:
            r = requests.get(json_url)
            if r.status_code in [404, 500, 501, 502, 503, 504, 405, 408, 410]:
                print json_url
        except:
            pass
        file_path = download(json_url)
        get_npm_packages(file_path)
    return all_package_metadata_json

def get_npm_packages(location):
    with open(location, 'rb') as json_file:
        json_data_dict = json.load(json_file)
        names = []
        licenses = []
        versions = []
        authors = []
        descriptions = []
        homepage_urls = []
        for key, value in json_data_dict['versions'].iteritems():
            names.append(value.get('sub_url'))
            licenses.append(value.get('license'))
            versions.append(value.get('version'))
            descriptions.append(value.get('description'))
            if value.get('author'):
                authors.append(value.get('author').get('sub_url'))
            homepage_urls.append((value.get('homepage')))
        print versions
        print authors
        print homepage_urls


def get_npm_package_objcects(all_json_url):
    file_path = download(all_json_url)
    packages = list(get_npm_names(file_path))
    print len(packages)
    print packages[0]

get_npm_package_objcects('https://registry.npmjs.org/-/all/static/all.json')
