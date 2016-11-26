#import data
import csv
with open('data_unique_jobs.csv','rb') as f:
    reader=csv.reader(f)
    list = map(tuple, reader)

#filter job code, job title, and job group
list2 = [0, 1, 2, 3]
data_filtered=[]
for l in list:
    if l[3].__contains__('detailed'):
        data_filtered.append([l[i] for i in list2])

job_title=[]
for data in data_filtered:
    job_title.append(data[2])

#remove stopwords and commas
stopwords = ['and','Other','All','Including','Except']
cleaned = []
for job in job_title:
    splitwords=job.split()
    cleanedwords = [word for word in splitwords if word not in stopwords]
    cleanedwords = ' '.join(cleanedwords)
    cleanedwords = cleanedwords.replace(",","")
    cleaned.append(cleanedwords)

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
