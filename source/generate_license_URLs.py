import urllib,csv


"""
given csv file consists of 2 columns without headers.
first column - github homepage URLs
second column - required version
output:
homepageurls.txt - list of homepage urls for a given version
licenseurls.txt - list of license urls for the genrated homepage urls
"""
homepageurls=[]
licenseurls = []
def generateurls(file_name):
    csvreader = csv.reader(open('C:\\Users\\nexB\\Documents\\testingurls.csv','rb'))
    homeurl=[]
    versions=[]
    for eachline in csvreader:
        homeurl.append(eachline[0].rstrip())
        versions.append(eachline[1].rstrip())
    treestrings = ['/tree/','/tree/v','\\tree\\V']
    for i in range(len(homeurl)):
        for eachstring in treestrings:
            if geturlstatus(homeurl[i] + eachstring + versions[i]) in (400,404):
                pass
            else:
                homepageurls.append(homeurl[i] + eachstring + versions[i])
                break
    
    writetofile('homepageurls.txt',homepageurls)
    generatelicenseurls()
    
def generatelicenseurls():
    licensestrings = ['/license','/LICENSE','/License','/license.txt','/LICENSE.txt']
    for eachurl in homepageurls:
        if eachurl.find('unable to find any valid URL')>-1:
            licenseurls.append('unable to find any license url')
        else:
            urladded = 0
            for eachstring in licensestrings:
                if geturlstatus(eachurl + eachstring) in (400,404):
                    pass
                else:
                    urladded = 1
                    licenseurls.append(eachurl+eachstring)
                    break
            if urladded == 0:
                if checkinreadme(eachurl)==False:
                    pass
                else:
                    pass        
    writetofile('licenseurls.txt', licenseurls)
            
def checkinreadme(url):
    readmestrings = ['/README.md','/README.MD','/README','/readme.md','/readme']
    for i in range(len(readmestrings)):
        if geturlstatus(url+readmestrings[i]) in (400,404):
            pass
        else:
            if checkforlicenseinreadme(url + readmestrings[i]) == True:
                licenseurls.append(url + readmestrings[i])
                return True
            else:
                licenseurls.append('unable to find any license URL')
                return False 
           
def checkforlicenseinreadme(url):
    htmlcode = urllib.urlopen(url,)
    htmldata=htmlcode.read()
    htmldata = htmldata.lower()
    if htmldata.find('license')>-1:
        return True
    else:
        return False
    
          
def writetofile(outputfile,data):
    filewriter = open(outputfile,'wb')
    for eachline in data:
        filewriter.write(eachline + '\n')           
def geturlstatus(givenurl):
    url_status = urllib.urlopen(givenurl)
    return url_status.getcode()

if __name__=='__main__':
    import sys
    file_name=sys.argv[0]
    generateurls(file_name)
    