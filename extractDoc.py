# Opening .CSV file to be read
import csv
import os
import time

print(time.perf_counter())

#Reading Excel file
fpath = os.path.join(os.getcwd(), "training.csv")
fs = csv.reader(open(fpath, newline='\n'))
rows = []

#Extract data from sparse Excel file while ignoring 0s
for r in fs:
    tmp = {}
    counter = 0
    for ea in r:
        if ea != '0':
            tmp1 = str(counter)
            tmp[tmp1] = ea
        counter += 1
    rows.append(tmp)

print(time.perf_counter())

#select a row you wish to print starting from 0
rn = 3

print(end = '\n')
print(rows[rn])
print(len(rows[rn]))
print(time.perf_counter())

with open("vocabulary.txt", "r") as file:
    features = file.read().splitlines()

#Print features of excel file
print(features)
print(time.perf_counter())

"""for ea in rows[rn].keys():
    tmp2 = int(ea)
    if tmp2 > 0 and tmp2 < 61189:
        print(features[tmp2 - 1], end = " ")
"""