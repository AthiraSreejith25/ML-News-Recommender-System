import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('corpus.csv', 'r')
reader = csv.DictReader(csvfile)
mongo_client=MongoClient()
db=mongo_client.reco
db.corpus.drop()

header= ['category', 'headline', 'date', 'content', 'keywords', 'link']

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.corpus.insert_one(row)
