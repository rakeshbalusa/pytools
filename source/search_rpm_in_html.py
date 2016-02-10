import urllib
import csv
urls = [
    'http://download.opensuse.org/pub/opensuse/ports/aarch64/distribution/13.1/repo/oss/suse/aarch64',
    'http://download.opensuse.org/repositories/home:/nocheck/SLE_12/x86_64',
    'http://download.opensuse.org/repositories/Base:/build/standard/x86_64',
    'http://download.opensuse.org/repositories/network:/samba:/MAINTAINED:/SLE_12/SLE_12/x86_64,http://suse.mirrors.tds.net/pub/opensuse/ports/ppc/distribution/13.2/repo/oss/suse/ppc',
    'http://download.opensuse.org/repositories/games/openSUSE_13.1/x86_64',
    'http://download.opensuse.org/repositories/home:/Alexander_Naumov:/SLE12/SLE_12_GA/x86_64http://download.opensuse.org/repositories/security:/SELinux/SLE_11_SP4/i586',
    'http://download.opensuse.org/ports/armv7hl/distribution/13.1/repo/oss/suse/armv7hl',
    'http://suse.mirrors.tds.net/pub/opensuse/ports/update/13.2/armv7hl',
    'http://download.opensuse.org/repositories/openSUSE:/42/images/repo/openSUSE-42.1-x86_64-Build0008-Media1/suse/x86_64',
    'http://download.opensuse.org/repositories/home:/nocheck/SLE_12/x86_64',
    'http://suse.mirrors.tds.net/pub/opensuse/ports/ppc/distribution/13.2/repo/oss/suse/ppc',
    'http://download.opensuse.org/tumbleweed/repo/src-oss/suse/src',
    'http://download.opensuse.org/distribution/13.1/repo/oss/suse/x86_64',
    'http://ftp.mirrorservice.org/sites/download.opensuse.org/update/13.1/x86_64',
    'http://download.opensuse.org/repositories/windows:/mingw:/win32/openSUSE_Factory/noarch',
    'http://ftp.mirrorservice.org/sites/download.opensuse.org/update/13.2-test/i586',
    'http://download.opensuse.org/repositories/openSUSE:/42/images/repo/openSUSE-42.1-x86_64-Build0008-Media1/suse/x86_64',
    'http://download.opensuse.org/update/13.2/src',
    'http://download.opensuse.org/repositories/home:/jhindel/openSUSE_13.2/x86_64',
    'http://anorien.warwick.ac.uk/mirrors/download.opensuse.org/repositories/network:/samba:/TESTING/openSUSE_12.3/x86_64',
    'http://download.opensuse.org/distribution/13.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/repositories/home:/nocheck/SLE_12/x86_64',
    'http://download.opensuse.org/repositories/Virtualization:/openSUSE42.1/SLE_12/x86_64',
    'http://download.opensuse.org/ports/ppc/distribution/13.1/repo/oss/suse/ppc64',
    'http://download.opensuse.org/repositories/home:/aevseev/CentOS7/src',
    'http://download.opensuse.org/repositories/openSUSE:/42/images/repo/openSUSE-42.1-x86_64-Build0008-Media1/suse/x86_64',
    'http://download.opensuse.org/repositories/network:/wicked:/factory/openSUSE_13.1_Update/x86_64',
    'http://download.opensuse.org/ports/aarch64/distribution/13.1/repo/oss/suse/aarch64',
    'http://download.opensuse.org/distribution/leap/42.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/repositories/security:/SELinux/SLE_12/x86_64',
    'http://download.opensuse.org/distribution/42.1/repo/non-oss/suse/x86_64',
    'http://download.opensuse.org/distribution/13.2/repo/non-oss/suse/x86_64',
    'http://download.opensuse.org/distribution/13.1/repo/non-oss/suse/x86_64',
    'http://download.opensuse.org/distribution/12.3/repo/non-oss/suse/x86_64',
    'http://download.opensuse.org/distribution/12.2/repo/non-oss/suse/x86_64',
    'http://download.opensuse.org/distribution/12.1/repo/non-oss/suse/x86_64',
    'http://download.opensuse.org/distribution/11.4/repo/non-oss/suse/x86_64',
    'http://download.opensuse.org/distribution/42.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/distribution/13.2/repo/oss/suse/x86_64',
    'http://download.opensuse.org/distribution/13.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/distribution/12.3/repo/oss/suse/x86_64',
    'http://download.opensuse.org/distribution/12.2/repo/oss/suse/x86_64',
    'http://download.opensuse.org/distribution/12.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/distribution/11.4/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/42.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/13.2/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/13.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/12.3/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/12.2/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/12.1/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/11.4/repo/oss/suse/x86_64',
    'http://download.opensuse.org/debug/distribution/42.1/repo/oss/suse/noarch',
    'http://download.opensuse.org/debug/distribution/13.2/repo/oss/suse/noarch',
    'http://download.opensuse.org/debug/distribution/13.1/repo/oss/suse/noarch',
    'http://download.opensuse.org/debug/distribution/12.3/repo/oss/suse/noarch',
    'http://download.opensuse.org/debug/distribution/12.2/repo/oss/suse/noarch',
    'http://download.opensuse.org/debug/distribution/12.1/repo/oss/suse/noarch',
    'http://download.opensuse.org/debug/distribution/11.4/repo/oss/suse/noarch',
    'http://download.opensuse.org/distribution/42.1/repo/non-oss/suse/noarch',
    'http://download.opensuse.org/distribution/13.2/repo/non-oss/suse/noarch',
    'http://download.opensuse.org/distribution/13.1/repo/non-oss/suse/noarch',
    'http://download.opensuse.org/distribution/12.3/repo/non-oss/suse/noarch',
    'http://download.opensuse.org/distribution/12.2/repo/non-oss/suse/noarch',
    'http://download.opensuse.org/distribution/12.1/repo/non-oss/suse/noarch',
    'http://download.opensuse.org/distribution/11.4/repo/non-oss/suse/noarch',
    'http://download.opensuse.org/distribution/42.1/repo/oss/suse/noarch',
    'http://download.opensuse.org/distribution/13.2/repo/oss/suse/noarch',
    'http://download.opensuse.org/distribution/13.1/repo/oss/suse/noarch',
    'http://download.opensuse.org/distribution/12.3/repo/oss/suse/noarch',
    'http://download.opensuse.org/distribution/12.2/repo/oss/suse/noarch',
    'http://download.opensuse.org/distribution/12.1/repo/oss/suse/noarch',
    'http://download.opensuse.org/distribution/11.4/repo/oss/suse/noarch',
    'http://download.opensuse.org/update/42.1/x86_64',
    'http://download.opensuse.org/update/13.2/x86_64',
    'http://download.opensuse.org/update/13.1/x86_64',
    'http://download.opensuse.org/update/12.3/x86_64',
    'http://download.opensuse.org/update/12.2/x86_64',
    'http://download.opensuse.org/update/12.1/x86_64',
    'http://download.opensuse.org/update/11.4/x86_64',
    'http://download.opensuse.org/update/42.1/x86_64',
    'http://download.opensuse.org/update/13.2/x86_64',
    'http://download.opensuse.org/update/13.1/x86_64',
    'http://download.opensuse.org/update/12.3/x86_64',
    'http://download.opensuse.org/update/12.2/x86_64',
    'http://download.opensuse.org/update/12.1/x86_64',
    'http://download.opensuse.org/update/11.4/x86_64',
    'http://download.opensuse.org/update/42.1/noarch',
    'http://download.opensuse.org/update/13.2/noarch',
    'http://download.opensuse.org/update/13.1/noarch',
    'http://download.opensuse.org/update/12.3/noarch',
    'http://download.opensuse.org/update/12.2/noarch',
    'http://download.opensuse.org/update/12.1/noarch',
    'http://download.opensuse.org/update/11.4/noarch',
    'http://download.opensuse.org/update/42.1/noarch',
    'http://download.opensuse.org/update/13.2/noarch',
    'http://download.opensuse.org/update/13.1/noarch',
    'http://download.opensuse.org/update/12.3/noarch',
    'http://download.opensuse.org/update/12.2/noarch',
    'http://download.opensuse.org/update/12.1/noarch',
    'http://download.opensuse.org/update/11.4/noarch',
    'http://yum.postgresql.org/srpms/9.3/redhat/rhel-6.5-x86_64',
    'http://download.opensuse.org/repositories/Cloud:/OpenStack:/Kilo/SLE_12/x86_64',
    'http://opensuse.mirror.ac.za/distribution/leap/42.1-Current/repo/oss/suse/x86_64',
    'http://download.opensuse.org/repositories/Cloud:/OpenStack:/Kilo/SLE_12/noarch',
    'http://download.opensuse.org/repositories/Cloud:/OpenStack:/Kilo/SLE_12/src',
    'http://download.opensuse.org/repositories/Cloud:/OpenStack:/Kilo/SLE_12/x86_64',
    'http://download.opensuse.org/repositories/Cloud:/OpenStack:/Kilo/SLE_12/noarch',
    'http://download.opensuse.org/distribution/13.1/repo/oss/suse/x86_64',
    'http://ftp.twaren.net/Linux/OpenSuSE/repositories/server:/http/SLE_12/x86_64',
    'http://download.opensuse.org/distribution/12.3/repo/oss/suse/x86_6'
    ]
url_string = []
for url in urls:
    urllib.urlretrieve(url, "replacetest.txt")
    with open("replacetest.txt", 'rb') as repl_file:
        lines = []
        for line in repl_file:
            line = line.strip()
            lines.append(line)
        url_string.append(lines)

rpms = []
with open('C:\\doc\\missing_rpms\\replace\\replace_test.csv','rb') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')
    for line in csv_read:
        rpms.append(line[0])
temp_dict = {}
for rpm in rpms:
    temp_dict[rpm] = ''




for rpm in rpms:
    temp_list = []
    for string in url_string:
        temp = ''.join(string)
        if temp.find(rpm) >= 0:
            temp1 = temp[temp.find(rpm):temp.find(rpm) + 50]
            if 'x86_64' in temp1 or 'noarch' in temp1:
                temp_list.append(temp1)
    value = '\n'.join(temp_list)
    temp_dict[rpm] = value

with open('C:\\doc\\missing_rpms\\replace\\search_results.csv', 'wb') as write:
    write_csv = csv.writer(write, delimiter=',')
    write_csv.writerows(zip(temp_dict.keys(), temp_dict.values()))
