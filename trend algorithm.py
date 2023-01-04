import csv
from collections import Counter

#upper control limit values (mean + 3 std devs)
HRUCL = 0
HRVUCL 0
SPO2UCL = 0
GSRUCL = 0
TEMPUCL = 0

#lower control limit values (mean - 3 std devs)
HRLCL = 0
HRVLCL = 0
SPO2LCL = 0
GSRLCL = 0
TEMPLCL = 0

#mean values
HRmean = 0
HRVmean = 0
SPO2mean = 0
GSRmean = 0
TEMPmean = 0

#standard deviation values
HRSTD = 0
HRVSTD = 0
SPO2STD = 0
GSRSTD = 0
TEMPSTD = 0

with open('stressData.csv') as file:
    csv_reader = csv.reader(files)
    #skip header
    next(csv_reader)
    
    #preform calculations
    for line in csv_reader:
        line[0]