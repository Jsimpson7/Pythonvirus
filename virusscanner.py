# Virus scan program
import csv
import glob
import re
import os
import sys

# Scan for signatures just like Symantec or other antivirus software
def checkForSignatures():
    print("###### Checking for virus signatures ######")

    # Get all programs in the directory
    programs = glob.glob("*.py")

    # Get the current script name
    scanner_file = os.path.basename(sys.argv[0])  # Just the filename, not the path

    # Exclude the scanner itself
    programs = [p for p in programs if p != scanner_file]

    for p in programs:
        thisFileInfected = False
        file = open(p, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            if re.search("# starting virus code", line):
                # Found a virus
                print("!!!!! Virus found in file " + p)
                thisFileInfected = True
                break  # Stop checking after finding the virus

        if not thisFileInfected:
            print(p + " appears to be clean")

    print("###### End section ######")
def getFileData():

    programs = glob.glob("*.py")
    programList = []
    for p in programs:
        programSize = os.path.getsize(p)
        programModified = os.path.getmtime(p)
        programData =[p, programSize, programModified]
        programList.append(programData)
    return programList
def WriteFileData(programs):
    if (os.path.exists("fileData.txt")):
        return
    with open("fileData.txt", "w") as file:
        wr = csv.writer(file)
        wr.writerows(programs)
def checkForChanges():
    print("###### Checking for heuristic changes in the files ######")


    with open("fileData.txt", "r") as file:
        fileList = file.read().splitlines()
    originalFileList = []
    for each in fileList:
        items = each.split(',')
        originalFileList.append(items)

    currentFileList = getFileData()

    for c in currentFileList:
        for o in originalFileList:
            if c[0] == o[0]:
                if (str(c[1]) != str(o[1] or str(c[2]) != str(o[2]))):
                    print("\n#####\nAlert. File mismatch!")
                    print("current values = " + str(c))
                    print("original values = " + str(o))
                else:
                    print("file " + c[0] + "appears to be unchanged")

    print("finished checking changes in files")

WriteFileData(getFileData())
checkForSignatures()
checkForChanges()


