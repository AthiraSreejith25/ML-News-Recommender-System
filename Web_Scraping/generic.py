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


def get_article_links(page_url, tag): #gets the links of articles from page

        req = requests.get(indiv_url, proxies=proxy_dict)
        pg = bs(req.content, 'html.parser')
        findings = pg.find_all(class_=tag)

        links = [i.a.get('href') for i in findings]

        return links

def get_article_data(article_url, tags):

	pass


#proxy settings
#http_proxy, https_proxy = None, None
http_proxy, https_proxy = 'http://172.16.2.250:3128', 'https://172.16.2.250:3128' #set variables to the desired proxy and to None if none
proxy_dict = {'http':http_proxy, 'https':https_proxy}

news_src = 'india_today'
cat_types = [['lifestyle/health','trending-news','cities','lifestyle','binge-watch','fact-check','data-intelligence-unit','india','business','world','science'], ['happiness-quest','movies','technology','newsmo','sports','television','education-today']]

sys('mkdir {}'.format(news_src))
sys('mkdir {}/raw'.format(news_src))
