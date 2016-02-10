import re

line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

searchObj = re.search(r'dogs', line, re.M | re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"
urls = ['http://download.opensuse.org/distribution/13.2/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.2/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.1/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.2/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.1/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/update/42.1/suse/repodata/repomd.xml',
'http://download.opensuse.org/update/42.1/suse/repodata/repomd.xml',
'http://download.opensuse.org/update/42.1/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/debug/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.2/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/non-oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.2/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/update/42.1/suse/repodata/repomd.xml',
'http://download.opensuse.org/update/42.1/suse/repodata/repomd.xml',
'http://download.opensuse.org/update/42.1/suse/repodata/repomd.xml',
'http://download.opensuse.org/update/42.1/suse/repodata/repomd.xml',
'http://opensuse.mirror.ac.za/distribution/leap/42.1-Current/repo/oss/suse/repodata/repomd.xml',
'http://download.opensuse.org/repositories/Cloud:/OpenStack:/Kilo/SLE_12/repodata/repomd.xml',
'http://download.opensuse.org/distribution/13.1/repo/oss/suse/repodata/repomd.xml',
'http://ftp.redhat.com/pub/redhat/linux/enterprise/6Server/en/os/SRPMS/repodata/repomd.xml',
'http://quattorsrv.lal.in2p3.fr/packages/os/sl6/epel/repodata/repomd.xml',
'http://www.pgpool.net/repodata/repomd.xml',
'http://webmin.mirror.somersettechsolutions.co.uk/yum/repodata/repomd.xml',
'http://mirrors.usc.edu/pub/linux/distributions/centos/7.1.1503/updates/x86_64/repodata/repomd.xml',
'http://ftp.pbone.net/mirror/ftp.scientificlinux.org/linux/scientific/6.0/i386/updates/security/repodata/repomd.xml',
'http://ftp.pbone.net/mirror/ftp.scientificlinux.org/linux/scientific/6.0/x86_64/updates/security/repodata/repomd.xml',
'http://download.opensuse.org/distribution/12.3/repo/non-oss/suse/repodata/repomd.xml']
new_list = list(set(urls))
for url in new_list:
    print url
