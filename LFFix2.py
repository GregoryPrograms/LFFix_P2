import os, tkinter
from tkinter import Tk, filedialog
from pathlib import Path,PurePath
BADDICTIONARY = '#,/`~'
def fileFix(fileList):
    for files in fileList:
        fixedFile = files[0].translate({ord(k):None for k in BADDICTIONARY})
        os.rename(PurePath(files[1])/files[0], PurePath(files[1])/fixedFile)

def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to trim file names...'))
    fileList = []
    for root, _, files in os.walk(dirPath):
        for name in files:
            fileObj = [name, root]
            fileList.append(fileObj)
    fileFix(fileList)
if(__name__ == "__main__"):
    main()