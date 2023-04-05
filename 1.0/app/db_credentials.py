# DB
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

# Functions

def delete_data(title):
	c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
	conn.commit()


def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def login_user_safe2(username,password):
	c.execute("SELECT * FROM userstable WHERE username= '%s' AND password = '%s'"),(username, password);
	data = c.fetchall()
	return data
