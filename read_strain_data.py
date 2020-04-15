#!/usr/bin/python
# Python code to read in the strain data

import pandas as pd
import pymysql

# open the file into dataframe
data = pd.read_excel('/home/students_20/mrozman/Proj/Database_Idea_1.xlsx')

# change dataframe column names, and remove unnecessary columns
data.rename(str.lower, axis = 'columns', inplace=True)
data.columns = data.columns.str.replace(' |/', '_', regex=True)
data.columns = data.columns.str.replace('\(|\)', '', regex=True)
data.rename(columns={'temp__c_dsmz':'tempc_dsmz','media_obs_2':'media_obs2', 'media_obs_3':'media_obs3', 'lab_location':'lab'}, inplace=True)

# remove cols we dont need
data = data.drop(columns=['box', 'lab', 'media_komodo', 'media_dsmz', 'tempc_dsmz',	'media_obs', 'media_obs2', 'media_obs3'])
data = data.fillna('NULL')
cols = ", ".join([str(i) for i in data.columns.tolist()])

# connect to db
connection = pymysql.connect(host="bioed.bu.edu", user="mrozman", password="mrozman", db="groupC", port=4253)
cursor = connection.cursor()

# insert rows
data = data.applymap(str)
for i in range(len(data)):
	row = tuple(data.iloc[i, :])
	sql = "INSERT INTO Strain (" + cols + ") VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(row)
	cursor.execute(sql)
	connection.commit()