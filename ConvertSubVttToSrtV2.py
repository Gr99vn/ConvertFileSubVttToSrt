import glob, os
import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.withdraw()

def getFilePath():
    file_path = filedialog.askopenfilenames(filetypes = (('VTT Files', '*.vtt'), ("All Files","*.*")))
    # file_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return list(file_path)
def getFilePathByFolder():
    folderPath = filedialog.askdirectory()
    os.chdir(folderPath)
    fileList = []
    for file in glob.glob("*.vtt"):
        fileList.append(file)
    return fileList

def doConvert(fileIn, fileOut):
    fin = open(fileIn,"r")
    fout = open(fileOut,"w")
    # content = fin.read()
    # print(content)
    newIndex = 0
    oldIndex = 1
    numberSub = 1 
    for line in fin:
        if newIndex == 0:
            newIndex += 1
            continue 
        if oldIndex + 3 == newIndex:
            numberSub += 1
            oldIndex = newIndex
        if line.isspace():
            fout.write(str(numberSub) + '\n')
        if oldIndex + 1 == newIndex:
            strIn = line.split(' --> ')
            match = re.sub(r'[.]{1}', ',', strIn[0])
            match = re.sub(r'^00', '00:00', match)
            strOut = match
            match = re.sub(r'[.]{1}', ',', strIn[1])
            match = re.sub(r'^00', '00:00', match)
            strOut += ' --> ' + match
            fout.write(strOut)
        if oldIndex + 2 == newIndex:
            fout.write(line + '\n')
        newIndex += 1

def makeFileName(fileBase):
    newFName = re.sub(r'.vtt$', '', fileBase) 
    return  newFName + '.srt'

print('\n\n  -->  Take one of two option below:')
print('  1. Choose one or many files you want to convert to .srt.')
print('  2. Choose one folder, then we will convert all the files .vtt in this folder.')

key = input('\n  -->  Enter your choice (1 or 2): ')
if int(key) == 1:
    print('  -->  Let\'s start with choosing file.')
    listFile = getFilePath()
elif int(key) == 2:
    print('  -->  Let\'s start with choosing folder.')
    listFile = getFilePathByFolder()

count = 0
for filePath in listFile:
    fileOut = makeFileName(filePath)
    doConvert(filePath, fileOut)
    print('  -->  Convert file', filePath, 'to', fileOut, 'successfully!')
    count += 1
print('\n\n  ==>  Converted successfully total [', count, '] file.')
print('\n\n  Author: GhostRyuki')
input('  -->  Press Enter to exit.')