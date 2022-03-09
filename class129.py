import csv 

data=[]

with open('dataset_2.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

header=data[0]
planet_data=data[1:]
#converting all planet name to lower case
for data_point in planet_data:
    data_point[2]=data_point[2].lower()

#sorting planet names in alphabetical order
#lambda is a keyword use to define a fuction which has no name
planet_data.sort(key=lambda planet_data:planet_data[2])

with open('dataset_2_sorted.csv','a+') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)
