#!/bin/python3
#The above line is called a Shebang and it tells the shell to determine with what to run this file.

#importing required packages
from os import system as sys #to execute shell commands
import requests #to make HTTP requests
import time #to use time.sleep for delay
import random #to randomise delays
from bs4 import BeautifulSoup as bs #package for webscraping
import csv #to make csv output file
import re #to search patterns and edit strings
import mysql.connector #to make MySQL db using python


#proxy settings
#http_proxy, https_proxy = None, None
http_proxy, https_proxy = 'http://172.16.2.250:3128', 'https://172.16.2.250:3128' #set variables to the desired proxy and to None if none
proxy_dict = {'http':http_proxy, 'https':https_proxy}

site = 'https://www.indiatoday.in'

sys('mkdir india_today')
sys('mkdir india_today/raw')


ez_scrape_catgries = ['lifestyle/health','trending-news','cities','lifestyle','binge-watch','fact-check','data-intelligence-unit','india','business','world','science']
messy_pages_catgries = ['happiness-quest','movies','technology','newsmo','sports','television','education-today']

'''
note that an article can be under multiple categories, so avoid duplicates
what to do about sub-cat like lifestyle-->health?

Future scope for real time: https://www.simplified.guide/scrapy/scrape-rss
'''

def date_conv(str_, mode=1):

	months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

	list_ = str_.split(' ')

	m = months.index(list_[0].lower()[:3])+1
	d = int(re.sub('[^\d]+','',list_[1]))
	y = int(re.sub('[^\d]+','',list_[2]))

	return (d, m, y)

def get_article_links(page_url, tag): #gets the links of articles from page

	time.sleep(random.randrange(1,2))
	req = requests.get(page_url, proxies=proxy_dict)
	pg = bs(req.content, 'html.parser')
	findings = pg.find_all(class_=tag)

	links = [i.a.get('href') for i in findings]

	return links

def get_article_data(article_link):

	data = []

	time.sleep(random.randrange(1,2))
	req = requests.get(article_link, proxies=proxy_dict)
	pg = bs(req.content, 'html.parser')

	#headline
	x  = pg.find("h1", itemprop='headline')

	if x != None:
		data.append(x.get_text())
	else:
		data.append('NA')

	#date
	x = pg.find(class_="pubdata")

	if x != None:
		data.append(date_conv(x.get_text()))
	else:
		data.append('NA')

	#content
	x = pg.find("div", attrs={'itemprop':'articleBody'})

	if x != None:
		data.append(x.get_text())
	else:
		data.append('NA')


	#keywords
	x = pg.find("meta", attrs={'name':"keywords"})

	if x != None:
		data.append((x.get('content')).split(","))
	else:
		data.append('NA')

	return data


fields = ['SN', 'category', 'headline', 'date', 'content', 'keywords', 'link']

def categoriterator(catlist):

	for category in catlist:

		sys('mkdir india_today/raw/{}'.format(category))

		url = 'https://www.indiatoday.in/{}'.format(category)
		main_pg = requests.get(url, proxies=proxy_dict) #gets the required page and stores it as a requests.models.Response object
		bs_page = bs(main_pg.content, 'html.parser') #parsed contents of main_pg

		#finding last page number
		class_num_pg = bs_page.find(class_='pager-last last')
		last_pg = int(class_num_pg.a.get('href').split("=")[1])


		#get links from first page
		article_links = get_article_links('https://www.indiatoday.in/{}'.format(category), 'detail')



		with open('./india_today/raw/{}/{}_1.csv'.format(category, category), 'w') as file:

			write = csv.writer(file)
			write.writerow(fields)

			SN = 1

			for link in article_links:

				write.writerow([SN, category] + get_article_data(site + link) + [site + link])
				SN += 1

				print(SN)


		for i in range(1,last_pg+1):

			print(category, ' {} out of {}'.format(str(i+1), str(last_pg)))

			article_links = get_article_links('https://www.indiatoday.in/{}?page={}'.format(category, str(i)), 'detail')


			with open('./india_today/raw/{}/{}_{}.csv'.format(category, category, str(i+1)), 'w') as file:

				write = csv.writer(file)
				write.writerow(fields)

				SN = 1

				for link in article_links:

					write.writerow([SN, category] + get_article_data(site + link) + [site + link])
					SN += 1

					print(SN)


categoriterator(['science'])


'''
fact-check till 84
Remove duplicates and assign article IDs
'''
