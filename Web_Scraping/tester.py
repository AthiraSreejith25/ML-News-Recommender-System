#importing required packages
from os import system as sys #to execute shell commands
import requests #to make HTTP requests
import time #to use time.sleep for delay
import random #to randomise delays
from bs4 import BeautifulSoup as bs #package for webscraping
import csv #to make csv output file
import re #to search patterns and edit strings
import mysql.connector #to make MySQL db using python


#http_proxy, https_proxy = None, None
http_proxy, https_proxy = 'http://172.16.2.250:3128', 'https://172.16.2.250:3128' #set variables to the desired proxy and to None if none
proxy_dict = {'http':http_proxy, 'https':https_proxy}



url = 'https://www.indiatoday.in/india'
main_pg = requests.get(url, proxies=proxy_dict) #gets the required page and stores it as a requests.models.Response object
bs_page = bs(main_pg.content, 'html.parser') #parsed contents of main_pg

articles = bs_page.find_all(class_='detail')

for i in articles:

#	print(i.a.get('href'),'\n\n\n')
	pass

'''
indiv_url = 'https://www.indiatoday.in/india?page={}'.format(1)
indiv_req = requests.get(indiv_url, proxies=proxy_dict)
indiv_pg = bs(indiv_req.content, 'html.parser')

articles = indiv_pg.find_all(class_='detail')

for i in articles:

	print(i.a.get('href'),'\n\n\n')
'''

url = 'https://www.indiatoday.in/india/story/chandigarh-municipal-corporation-passes-resolution-maintain-city-ut-status-1934827-2022-04-07'
req = requests.get(url, proxies=proxy_dict)
pg = bs(req.content, 'html.parser')

x = pg.find("h1", itemprop='headline')
headline = x.get_text()
print(x.get_text(),'\n\n')

x = pg.find(class_="pubdata")
print(x.get_text())

date = x.get_text()

x = pg.find("meta", attrs={'name':"keywords"})

keywords = (x.get('content')).split(",")
print(keywords)

category = 'whatever'

x = pg.find("div", attrs={'itemprop':'articleBody'})

content = x.get_text()

print(pg.find("coria"))

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def date_conv(str_, mode=1):

	list_ = str_.split(' ')

	m = months.index(list_[0].lower()[:3])+1
	d = int(re.sub('[^\d]+','',list_[1]))
	y = int(re.sub('[^\d]+','',list_[2]))

	return (d, m, y)

print(date)
print(date_conv(date))

#pg = bs_page.find(class_='pager-last last')

#print(pg.a.get('href').split("=")[1])

#left = str(class_num_pg)[str(class_num_pg).find("?page=")+len("?page="):]
#last_pg = int(left[:left.find('"')])

#print(last_pg)

