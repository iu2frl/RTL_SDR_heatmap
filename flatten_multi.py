#! /usr/bin/env python

import sys
from collections import defaultdict
import os.path
import csv

# todo
# interval based summary
# tall vs wide vs super wide output

def help():
    print("flatten.py")
    print("turns any rtl_power csv into a more compact summary")
    sys.exit()

if len(sys.argv) > 1:
    help()

#path = sys.argv[1]
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
print("Found " + str(len(newFilesList)) + " files")

sums = defaultdict(float)
counts = defaultdict(int)

def frange(start, stop, step):
    i = 0
    f = start
    while f <= stop:
        f = start + step*i
        yield f
        i += 1

progressCnt = 0
outFile = []

for listRow in newFilesList:
    print("[" + str(progressCnt) + "/" + str(len(newFilesList)) + "] " + " Opening file: " + str(listRow))
    for line in open(listRow):
        line = line.strip().split(', ')
        low = int(line[2])
        high = int(line[3])
        step = float(line[4])
        weight = int(line[5])
        dbm = [float(d) for d in line[6:]]
        for f,d in zip(frange(low, high, step), dbm):
            sums[f] += d*weight
            counts[f] += weight

    ave = defaultdict(float)
    for f in sums:
        ave[f] = sums[f] / counts[f]

    # Reconstruct original file format
    outRow = ["2022-08-14", "00:18:07", "430000000", "432000000", "976.56", "160"]
    for f in sorted(ave):
        if (float(f)<432.1):
            outRow[2] = "430000000"
            outRow[3] = "432000000"
        else:
            outRow[2] = "432000000"
            outRow[3] = "434000000"
        outRow.append(str(round(ave[f],2)))
        outFile.append(outRow)
        #print(outRow)
        #print(str(f) + "," + str(ave[f]))
    
print("Writing CSV file...")
# Write output to CSV
csvFile =  open("output3.csv", "w", newline='')
# create the csv writer
writer = csv.writer(csvFile)
#for row in dbSumAry:
# write a row to the csv file
writer.writerows(outFile)
# close the file
csvFile.close()
print("Done!")