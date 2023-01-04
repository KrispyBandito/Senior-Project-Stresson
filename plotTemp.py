import csv
import matplotlib.pyplot as plt

def showTemp():

    date = []          #x axis
    temp = []          #y axis

    with open('stressData.csv', 'r') as f:
        lines = csv.reader(f, delimiter=',')
        for row in lines:
            date.append(row[0])
            gsr.append(int(row[2]))
            
    plt.plot(date, gsr, color = 'g', linestyle = 'dashed', marker = 'o', label = "Temp Data")
    plt.xticks(rotation = 25)
    plt.xlable('Date')
    plt.ylabel('Temperature (F)')
    plt.title('Temp Trends', fontsize = 20)
    plt.grid()
    plt.legend()
    plt.show()
    return
    