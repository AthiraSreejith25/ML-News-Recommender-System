import csv, sqlite3
import streamlit as st
con = sqlite3.connect(':memory:',check_same_thread=False)
#con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('create virtual table t using fts5(id,category,headline,date,content,keywords,link,tokenize="porter unicode61");') # use your column names here

with open('corpus.csv','r',encoding='utf-8') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'],i['category'],i['headline'],i['date'],i['content'],i['keywords'],i['link']) for i in dr]

cur.executemany("INSERT INTO t (id,category,headline,date,content,keywords,link) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()

def search_news(query):

    q = ""
    qry = query.split()
    l = len(qry)
    temp = 0
    if l != 1:
        for i in qry:
            temp += 1
            if temp == l:
                q += i
                break
            q = q + i + ' AND' + ' '
        q = q + '*'
    else:
       q = qry[0] + '*'

#    st.text(q)
    
    r = db_execute_with_qry(q)
    return r


def db_execute_with_qry(q):
    res = cur.execute(f"""select *, rank
                      from t
                      where headline MATCH "{q}"
                      limit 5;""").fetchall()

    return res

def db_execute():
    res = cur.execute(f"""select *, rank
                      from t
                      limit 15;""").fetchall()

    return res

def db_execute_all():
    res = cur.execute(f"""select *, rank
                      from t;""").fetchall()

    return res
