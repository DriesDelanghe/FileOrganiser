import os
from datetime import datetime
from pathlib import Path
import shutil
import zipfile
import getpass


#def convertDate(timestamp):
#    d = datetime.utcfromtimestamp(timestamp)
#    formatedDate = d.strftime('%Y-%m-%d')
#    return formatedDate


def changeDir(destination):
    user = getpass.getuser()
    myDir = "c:/Users/"+user+"/" + destination
    return myDir
        
def moveFileToDir(Dir, file, fileType):
    p = Path(Dir + "\\" + fileType)
    try:
        p.mkdir()
    except FileExistsError as exc:
        print(exc)
    path = str(p)
    path = path.replace("\\", "/")
    
    dst = path + "/" + file.name
    src = myDir + "/" + file.name
    shutil.move(src, dst)
 
def zipFileHandler(dir, file):
    fileName = file.name 

    data_zip = zipfile.ZipFile(file, 'r')

    p = Path(dir + "\\" + 'zip')
    try:
        p.mkdir()
    except FileExistsError as exc:
        print(exc)

    path = str(p)
    path = path.replace("\\", "/")
    
    path = path + "/" + fileName
    
    data_zip.extractall(path)
    data_zip.close()

    src = src = myDir + "/" + file.name
    shutil.move(src, path)
    


def FormatList (dataTypeList):
    finalList = list()
    dataTypeList = [line.split(',') for line in dataTypeList.readlines()]
    for item in dataTypeList:
        item = item[0]
        finalList.append(item)

    
    return finalList

basePath = str(Path(__file__).parent)

imageTypes = open(basePath + "/imageTypes.txt", 'r')
imageTypesList = FormatList(imageTypes)
imageTypes.close()

documentTypes = open(basePath + "/documentTypes.txt", 'r')
documentTypesList = FormatList(documentTypes)
documentTypes.close()

audioTypes = open(basePath + "/audioTypes.txt", 'r')
audioTypesList = FormatList(audioTypes)
audioTypes.close()

videoTypes = open(basePath + "/videoTypes.txt")
videoTypesList = FormatList(videoTypes)
videoTypes.close()

user = getpass.getuser()
myDir = "c:/Users/"+user+"/Downloads"
    
with os.scandir(myDir) as entries:
    for entry in entries:
        if entry.is_file():
            entryName = entry.name
            fileType = entryName.split('.')
            fileType = fileType[-1]
            
            print(entryName, "\t", "file type:", fileType)
            
            if fileType in imageTypesList:
                newDir = changeDir("Pictures")
            elif fileType in documentTypesList:
                newDir = changeDir("Documents")
            elif fileType in audioTypesList:
                newDir= changeDir("Music")
            elif fileType in videoTypesList:
                newDir = changeDir("Videos")                
            else:
                newDir = myDir
            
            if fileType != 'zip':
                moveFileToDir(newDir, entry, fileType)
            else:
                zipFileHandler(myDir, entry)