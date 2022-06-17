import csv

df=[]
with open("lightestStars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        df.append(row)

starData = df[1:]

for data in starData:
    if data[2]=="" or data[3]=="" or data[4]=="":
        starData.remove(data)
    elif data[2]!="" or data[3]!="" or data[4]!="":
        radius=float(data[4])*0.102763
        data[4]=radius
        mass=float(data[3])*0.000954588
        data[3]=mass

df1=[]
with open("brightestStars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        df1.append(row)

headers = df1[0]
starData1 = df1[1:]

for data in starData1:
    if data[2]=="" or data[3]=="" or data[4]=="" or data[5]=="":
        starData1.remove(data)

with open("final.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(starData1)
    csvWriter.writerows(starData)