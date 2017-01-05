import csv
import sqlite3

def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    #print data[6][0]
    return data

def count_data(data):
    with open(data, 'r') as f:
	    y= csv.DictReader(f.read().splitlines())
	    count=0
	    for row in y:
		 data = row
		 count=count+1
	    print count 
        #data = [row for row in csv.reader(f.read().splitlines())]
    #print data[6][0]
    return count

def db_data():
    conn = sqlite3.connect('incdb.sqlite')
    cur = conn.cursor()
    cur.execute('Select count(*) from incident1 where assigned_to = "Beth Anglin"')
    row = cur.fetchone()
    row1=row[0]
    print row1
    conn.commit()
    return row1
data = "incident.csv"
db_data()	
count_data(data)
