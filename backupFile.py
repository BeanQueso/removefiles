import time
import os
import shutil

def main():
    path = input("enter the path you want to delete")
    days = 30
    seconds = time.time()-(days*24*60*60)
    deletedFolderCount = 0
    deletedFileCount = 0
    if (os.path.exists(path)):
        for rootFolder, folders, files in os.walk(path):

            if(seconds>=getFileOrFolderAge(rootFolder)):
                removeFolder(rootFolder)
                deletedFolderCount+=1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder,folder)

                    if(seconds>=getFileOrFolderAge(folderPath)):
                        removeFolder(folderPath)
                        deletedFolderCount+=1

                for file in files:
                    filePath = os.path.join(rootFolder, file)
                    
                    if(seconds>=getFileOrFolderAge(filePath)):
                        removeFile(filePath)
                        deletedFileCount+=1
        else:
            if(seconds>=getFileOrFolderAge(path)):
                remove_file(path)
                deletedFileCount+=1
    else:
        print('Path is not found', path)
        deletedFileCount+=1
    print('total folder deleted:', deletedFolderCount)
    print('total file deleted:', deletedFileCount)

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removeFolder(path):
    if(not shutil.rmtree(path)):
        print('folder is removed successfully', path)
    else:
        print('unable to remove the folder', path)

def removeFile(path):
    if(not os.remove(path)):
        print('file has been removed successfully')
    else:
        print('unable to remove the file')

main()


