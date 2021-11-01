import csv
import math 

with open('project.csv', newline='')as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    n = len(data)
    total = 0

    for d in data:
        total += int(d)
    
    mean = total/n
    return mean

squaredlist = []

for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredlist.append(a)

sum = 0

for s in squaredlist:
    sum = sum+s

result = sum/(len(data)-1)

stdDeviation = math.sqrt(result)

print('THE DEVIATION IS:'+ str(stdDeviation))