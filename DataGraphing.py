import csv
import matplotlib.pyplot as plt
import numpy as np
Data = []
with open('games.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        Data.append(line[2])
AveData = []
for item in Data:
    if Data[item] % 10 == 0:
        print(Data[int(item)])
        AveData.append(item)
print(len(Data))
#plt.plot(Data)
#plt.ylabel('Length of Game')
#plt.ylabel('Rank over Time')
#plt.show()