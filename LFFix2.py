import os, tkinter
from tkinter import Tk, filedialog
from pathlib import Path,PurePath
BADDICTIONARY = '#,/`~'
def foldFix(foldList):
    for folders in reversed(foldList):
        fixedFolder = folders[0].translate({ord(k):None for k in BADDICTIONARY})
        os.rename(PurePath(folders[1])/folders[0], PurePath(folders[1])/fixedFolder)

def fileFix(fileList):
    for files in fileList:
        fixedFile = files[0].translate({ord(k):None for k in BADDICTIONARY})
        os.rename(PurePath(files[1])/files[0], PurePath(files[1])/fixedFile)

def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to trim file names...'))
    fileList = []
    foldList = []
    for root, folders, files in os.walk(dirPath):
        for name in folders:
            foldObj = [name, root]
            foldList.append(foldObj)
        for name in files:
            fileObj = [name, root]
            fileList.append(fileObj)
    fileFix(fileList)
    foldFix(foldList)
if(__name__ == "__main__"):
    main()