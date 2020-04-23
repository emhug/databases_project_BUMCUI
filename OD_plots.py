import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cgi
import pymysql

# connect to database
connection = pymysql.connect(host='bioed.bu.edu',database='groupC',user='mrozman',password='mrozman',port=4253)
cursor = connection.cursor()

# source selections
source = '(1, 2, 3, 4, 5)'
media = '1'
strain = '7'

# get some data
query = """SELECT C_source, OD24hr, OD48hr, OD72hr FROM Experiment JOIN Source USING(source_id) WHERE strain_id = %s and media_id = %s and source_id in %s"""%(strain, media, source)

cursor.execute(query)
rows = cursor.fetchall()

# create a list to convert to pandas dataframe
data = []
for row in rows:
    data.append([row[0], row[1], row[2], row[3]])

data = pd.DataFrame(data, columns=['source', '24', '48', '72'])
data.set_index("source", inplace = True) 

data=data.transpose()

print(data)

sns.set()
sns.set_context(rc={"lines.linewidth": 2.5, "lines.linestyle":"--"})
ax=sns.lineplot(hue="source", data=data, markers=True)
ax.set(xlabel='Timepoint (hr)', ylabel='OD')