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

#remove stopwords
job = "Tax Examiners and Collectors, and Revenue Agents"
stopwords = ['and','Other','All','Including','Except']
splitwords = job.split()

resultwords = [word for word in splitwords if word not in stopwords]
result = ' '.join(resultwords)
print result

#remove comma
result_nocomma = result.replace(",","")
print result_nocomma

#count common words in 2 strings
s2 = "Public Relation Fundraising Managers"
length = len(result_nocomma.split())
count = 0
for i in range(length):
    word = result_nocomma.split(" ", length)[i]
    if word in s2:
        count= count+ 1
    else:
        count=count+0
print count
