import csv 

data1 = []
data2 = []

with open("dwarf_stars1.csv","r",encoding="utf8") as f:
    csvreader = csv.reader(f)
    
    for row in csvreader:
        data1.append(row)

with open ("unit_converted_stars.csv","r",encoding="utf8") as f:
    csvreader = csv.reader(f)

    for row in csvreader:
        data2.append(row)

headers1 = data1[0]
planetdata1 = data1[1:]

headers2 = data2[0]
planetdata2 = data2 [1:]

headers = headers1 + headers2
planet_data = []

for i in planetdata1:
    planet_data.append(i)

for a in planetdata2:
    planet_data.append(a)
    
with open ("total_stars.csv","w",encoding="utf8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)



