import csv
import matplotlib.pyplot as plt

date = []         #x axis
gsr = []          #y axis

with open('stressData.csv', 'r') as f:
    lines = csv.reader(f, delimiter=',')
    for row in lines:
        date.append(row[0])
        gsr.append(int(row[1]))
        
    plt.plot(date, gsr, color = 'g', linestyle = 'dashed', marker = 'o', label = "GSR Data")
    plt.xticks(rotation = 25)
    plt.xlable('Dates')
    plt.ylabel('GSR (Ohms)')
    plt.title('GSR Trends', fontsize = 20)
    plt.grid()
    plt.legend()
    plt.show()
    