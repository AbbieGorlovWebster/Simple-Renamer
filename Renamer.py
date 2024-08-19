from tkinter import filedialog
import shutil
import os

def open_file_selection():

    namesListFile = filedialog.askopenfile(title="Open List Containing File Names")

    namesList = namesListFile.readlines()

    outputDirectory = filedialog.askdirectory(title="Select Output Folder")

    for name in namesList :
        dialogueTitle = "Select File To Be Renamed " + name
        renameFileDirectory = filedialog.askopenfilename(title=dialogueTitle)

        renameFileExtension = os.path.splitext(renameFileDirectory)[1]

        outputFileDirectory = outputDirectory + "/" + name.replace("\n", "") + renameFileExtension

        shutil.copyfile(renameFileDirectory, outputFileDirectory)

open_file_selection()