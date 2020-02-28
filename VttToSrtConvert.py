import FilePath
from FilePath import getFilePath
from FileOperation import doConvert, makeFileName

listFile = getFilePath()

for filePath in listFile:
    doConvert(filePath, makeFileName(filePath))
