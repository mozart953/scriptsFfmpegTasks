import subprocess
import os

def executeCommand(entry1, entry2):
    fileName= os.path.abspath(entry1)
    fileOutput = os.path.join(fileName, entry2)
    comand = ['ffmpeg', '-f', 'concat',  '-i',  fileName, '-c', 'copy', fileOutput]
    subprocess.run(comand)



def mainFunc():
    absRoute = input("Write the file's absolute route: ")
    outputName = input("Write the file's output name: ")
    executeCommand(absRoute, outputName)

mainFunc()