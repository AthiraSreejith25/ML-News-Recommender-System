import csv
import os

#path = '/home/sklodowska/Desktop/ML/web_scraping/india_today/raw'
path = '/home/kalian/Desktop/Coding/Python/sem_8/IDC410/recommender/web_scraping/india_today_new/raw'

category = os.listdir(path)

final_csv = []
heading = 2 
content = 4

c,d = 0,0

for topic in category:
	#print(topic)
	#print(len(os.listdir('/home/sklodowska/Desktop/ML/web_scraping/india_today/raw/{}'.format(topic))))
	for file_i in os.listdir('{}/{}'.format(path,topic)):
		with open('{}/{}/{}'.format(path,topic,file_i), 'r') as file:
			rowss = list(csv.reader(file))[1:]
			#print(rowss[1][1:])
			for i in rowss:
				d += 1
				if i[content] == 'NA' or i[heading] == 'NA':
					#print(i[content],i[heading])
					c += 1
				if i[content] != 'NA' and i[heading] != 'NA':
					if len(i) == 7:
						final_csv.append(i[1:])


print(d,c+len(final_csv),len(final_csv))

with open('{}/corpus_new.csv'.format(path),'w') as file:
	write = csv.writer(file)
	write.writerows(final_csv)
