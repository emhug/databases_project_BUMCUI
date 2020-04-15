#!/usr/bin/python

import pandas as pd
import pymysql
import sys

# read in data
file_path = str(sys.argv[1])
data = pd.read_excel(file_path, skiprows = 5, usecols = "B,D:F,I")
# rename columns to match db
data.rename(columns={'24':'OD24hr', '48':'OD48hr', '72':'OD72hr', 'Carbon sources':'carbon'}, inplace = True)
data = data.fillna('NULL')
data = data[data.carbon != 'NULL']
data = data[data.carbon != 'threshold']

# connect to db
connection = pymysql.connect(host="bioed.bu.edu", user="mrozman", password="mrozman", db="groupC", port=4253)
cursor = connection.cursor()

# get command line arguments
strain_id = str(sys.argv[2])
media_id = str(sys.argv[3])
run_date = str(sys.argv[4])

# get all carbon sources and names
sql = "SELECT source_id, C_source FROM Source"
result = cursor.execute(sql)
sources = cursor.fetchall()
sources = dict((y, x) for x, y in sources)

# for each row, get the source id from the database
for i in range(len(data)):
 	row = tuple(data.iloc[i, :])
 	source_name = row[0]
 	source_id = sources[source_name]
 	values = (strain_id, media_id, source_id, run_date, row[1], row[2], row[3], row[4])
 	sql = "INSERT INTO Experiment (strain_id, media_id, source_id, run_date, OD24hr, OD48hr, OD72hr, notes) VALUES (%s, %s, %s, '%s', '%s', '%s', '%s', '%s')"%(values)
 	cursor.execute(sql)
 	connection.commit()
 	



