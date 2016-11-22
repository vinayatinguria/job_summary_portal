#import csv
with open('data_2015.csv','rb') as f:
    reader=csv.reader(f)
    list = map(tuple, reader)

#filter job code, job title, and job group
list2 = [3,4,5]
print list[1]
data_filtered = [[l[i] for i in list2] for l in list]
print data_filtered[1]

