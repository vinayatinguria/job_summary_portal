#import data
import csv
with open('data_2015.csv','rb') as f:
    reader=csv.reader(f)
    list = map(tuple, reader)

#filter job code, job title, and job group
list2 = [3, 4, 5]
print list[1]
data_filtered = [[l[i] for i in list2] for l in list]
#TODO: filter detailed jobs
data_filtered=data_filtered[:5]

job_title=[]
for data in data_filtered:
    job_title.append(data[1])

#remove stopwords and commas
stopwords = ['and','Other','All','Including','Except']
cleaned = []
for job in job_title:
    splitwords=job.split()
    cleanedwords = [word for word in splitwords if word not in stopwords]
    cleanedwords = ' '.join(cleanedwords)
    cleanedwords = cleanedwords.replace(",","")
    cleaned.append(cleanedwords)
print cleaned

#count common words in 2 strings
w= len(cleaned)
matrix = [[0 for x in range(w)] for y in range(w)]
for i in range(len(cleaned)):
    for j in range(len(cleaned)):
        words = cleaned[i].split()
        count=0
        if i != j:
            for word in words:
                if word in cleaned[j]:
                    count=count+1
        matrix[i][j]=count
print matrix
