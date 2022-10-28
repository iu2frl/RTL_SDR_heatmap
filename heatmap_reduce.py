import os.path
import csv
import math

inputFile =  open("./output2.csv", "rt", errors="ignore")
min = 9999.9
for logLine in inputFile:
    splitLine = logLine.split(",")
    for i in range(len(splitLine)):
        if (i>6):
            if (float(splitLine[i])<min):
                min = float(splitLine[i])
                print("New min: " + str(min))

