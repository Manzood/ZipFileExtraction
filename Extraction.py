from zipfile import ZipFile
import os

def getall(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_paths.append(filepath)
    return file_paths

directory = input ("Enter zip directory: ")
zipname = input ("Enter zip file name: ")
if directory[-1] != '/':
    directory+='/'
    newzipname = directory+zipname
else:
    newzipname = directory+zipname

#print(newzipname)

with ZipFile(newzipname, 'r') as zip:
    #zip.printdir()
    zip.extractall()
    
pwd = os.getcwd()
    
filepath = getall(pwd)

combined = []
totalcount = 0

print ("The following files will be opened: ")

for file in filepath:
    if zipname not in file and '.ipynb' not in file and 'output.txt' not in file:
        totalcount+=1
        print (file)
        f = open(file, 'r')
        output = open('output.txt', 'w')
        lines = f.read()
        #print (lines)
        for line in lines.split('\n'):
            combined.append(line)
        os.remove(file)
        #print (combined)

final = []

#print (totalcount)
#print (combined)
        
for i in combined:
    #print (i, combined.count(i))
    if combined.count(i) == totalcount and i not in final:
        final.append(i)

for i in final:
    output.write(i)
    output.write('\n')

output.close()

print("Successfully written text to output.txt (file present in the same directory as the program)")
