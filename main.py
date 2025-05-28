import subprocess
import os

def executeCommand(entry1, entry2):
    fileName= os.path.abspath(entry1)
    absoluteRoute = os.path.dirname(fileName)
    directoryOutput = os.path.join(absoluteRoute, entry2)
    fileOutput = os.path.join(fileName, entry2)
    comand = ['ffmpeg', '-f', 'concat',  '-i',  fileName, '-c', 'copy', directoryOutput]
    subprocess.run(comand)



def mainFunc():
    absRoute = input("Write the file's absolute route: ")
    outputName = input("Write the file's output name: ")
    executeCommand(absRoute, outputName)

mainFunc()