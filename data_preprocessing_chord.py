#import data
import csv
with open('data_2015.csv','rb') as f:
    reader=csv.reader(f)
    list = map(tuple, reader)

#filter job code, job title, and job group
list2 = [3,4,5]
print list[1]
data_filtered = [[l[i] for i in list2] for l in list]
print data_filtered[1]

#count common words in 2 strings
s="Public Relation and Fundraising Managers"
s2 = "Industrial Product Managers"
length = len(s.split())
count = 0
for i in range(length):
    word = s.split(" ", length)[i]
    if word in s2:
        count= count+ 1
    else:
        count=count+0
print count
