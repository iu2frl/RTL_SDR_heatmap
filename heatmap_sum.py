import os.path
import csv

# List containing all the files name. Each row contains file name and size
newFilesList = []
# Iterate over files in upload directory
for filename in os.listdir('csv'):
    f = os.path.join('csv', filename)
    # Checking if it is a file
    if os.path.isfile(f):
        # Filter only desired files type
        if (f.endswith('.csv')):
            newFilesList.append(f)

firstFile = True
dbSumAry = []

for listRow in newFilesList:
    # Process each file from input list
    print("Opening file: " + str(listRow))
    # Trying to detect input encoding
    inputFile =  open(listRow, "rt", errors="replace")
    lineCnt = 0
    for logLine in inputFile:
        splitRow = logLine.split(",")
        if (firstFile):
            newLogLine = []
            for i in range(len(splitRow)):
                newLogLine.append(str(splitRow[i]).replace("\n", ""))
            dbSumAry.append(newLogLine)
        else:
            i = 6
            while i < len(splitRow):
                #print("i: " + str(i))
                #print("lineCnt: " + str(lineCnt))
                #print("dbSumAry[lineCnt]: " + str(dbSumAry[lineCnt]))
                dataA = float(dbSumAry[lineCnt][i])
                dataB = abs(float(str(splitRow[i]).replace("\n","")))
                dbSumAry[lineCnt][i] = str(round(dataA + dataB, 2))
                i += 1
            lineCnt += 1
        #print("dbSumAry Rows: " + str(len(dbSumAry)))
        #print("dbSumAry Columns: " + str(len(dbSumAry[0])))
    #print(dbSumAry)
    firstFile = False

print("Writing CSV file...")
# Write output to CSV
csvFile =  open("output.csv", "w", newline='')
# create the csv writer
writer = csv.writer(csvFile)
#for row in dbSumAry:
# write a row to the csv file
writer.writerows(dbSumAry)
# close the file
csvFile.close()
print("Done!")