import csv

spo2Values[]
line = 0
index = 0
west1 = 0
west2 = 0
west3 = 0
west4 = 0

#add  spo2 values to arrray 
for spo2 in columns[1]:
    if spo2 != "":
        spo2Values[line] = spo2
    line =+ 1
#begin western electric rule 1
#parse through array to see if any array values fall outside 3 standard devs (UCL or LCL)  
for data in spo2Values:
    if data > UCL:
        West1 = 0        #western electric rule 1 fails
    else if data < LCL:
        West1 = 0        #western electric rule 1 fails
    else:
        West1 = 1        #western electric rule 1 passes
#begin western electric rule 2
#parse through array to check if any 2/3 consecutive points
for data in spo2Values:
    if line < 3: 
        spo2West2[line] = data
    else:                          #on 3rd point so reset line to 0 to check new set of  3 & west rule 2
        line = 0
        if spo2West2[0] > (SPO2MEAN+2*SPO2STD) || spo2West2[0] < (SPO2MEAN-2*SPO2STD)):       #if 1st point falls out of range
            break
        if spo2West2[1] > (SPO2MEAN+2*SPO2STD) || spo2West2[1] < (SPO2MEAN-2*SPO2STD):        #if 2nd point falls out of range
            break
        if spo2West2[2] > (SPO2MEAN+2*SPO2STD) || spo2West2[2] < (SPO2MEAN-2*SPO2STD):        #if 3rd point falls out of range
            break
    
        
                    
    
    line =+ 1
