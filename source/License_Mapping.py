#author - Rakesh Balusa (rbalusa@nexb.com)
#company - nexB
#create a csv file (license-keywords.csv) with license names in one column
#and corresponding keywords eperated by comma in the next column
#create an input.csv file with only one column which consists of user given
#names for licenses
#run 'License_Mapping.py' file
#check the 'output.csv' file


import csv
print "please wait..."
with open('license-keywords.csv','r') as csvfile:
    myReader=csv.reader(csvfile,delimiter=',',quotechar='"')
    i=0
    elements=[]
    for row in myReader:
        rowString=','.join(row)
        elements.append([])
        elements[i].append(rowString)
        for value in elements[i]:
            value=value.split(',')
            
        i=i+1
#print "i  :"+str(i)
newElements=[]
for each in elements:
    valueString=''.join(each)
    if valueString[len(valueString)-1]==',':
        valueString=valueString+'balusa'
    newElements.append(valueString.split(','))
elements=newElements
disp=0
'''
while disp<len(elements):
    print elements[disp]
    if disp>10:
        break
    disp=disp+1
'''
j=0
with open('All_Files_License_Expressions_and_Licenses.csv','r') as inputFile:
    inputReader=csv.reader(inputFile,delimiter=',',quotechar='"')
    finalResult=[]
    for row in inputReader:
        
        rowValue=''.join(row)
        
        while j<i:
            
            checkString=elements[j]
            
            result = [s.strip() for s in checkString]
            
            
            for eachValue in result:                    
                                
                value=rowValue.split(' and ')
                for each in value:
                    if each==eachValue:
                        
                        value[value.index(each)]=result[0]
                rowValue=' and '.join(value)
            
                
                    

            j=j+1

        j=0
        finalResult.append(rowValue)
            
            
            
        
print "check the output.csv file: "
que=1
#print "length : "+str(len(finalResult))




with open('output.csv', 'w') as handle:
    handle.write('\n'.join(finalResult))
    

    
        
            
        
        
