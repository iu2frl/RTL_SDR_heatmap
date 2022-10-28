import os.path
import csv
import math

inputFile =  open("./output.csv", "rt", errors="ignore")
newFile = []
for logLine in inputFile:
    splitLine = logLine.split(",")
    for i in range(len(splitLine)):
        if (i>6):
            if (math.isnan(float(splitLine[i]))):
                try:
                    splitLine[i] = str(splitLine[i-1])
                except:
                    print("err")
    newFile.append(splitLine)

print("Writing CSV file...")
# Write output to CSV
csvFile =  open("output2.csv", "w", newline='')
# create the csv writer
writer = csv.writer(csvFile)
#for row in dbSumAry:
# write a row to the csv file
writer.writerows(newFile)
# close the file
csvFile.close()
print("Done!")