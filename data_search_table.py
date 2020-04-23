#!/usr/local/Python-3.7/bin/python
import cgi
import pymysql

# retrieve form data, if any
form = cgi.FieldStorage()

#check if form data is returned
if form:

	# Connect to the database
	connection = pymysql.connect(host='bioed.bu.edu',database='groupC',user='mrozman',password='mrozman',port=4253)
	cursor = connection.cursor()

	# check if submit button was clicked
	submit = form.getvalue("submit")
	if submit:
		#get the species
		species = form.getvalue("species")
		strain = form.getvalue("strain")
		media = form.getvalue("media")
		#specify the query 
		query = """
		SELECT OD24hr, OD48hr, OD72hr 
		FROM Experiment
		WHERE strain_id IN (SELECT strain_id 
							FROM Strain 
							WHERE species = '%s' and (strain = '%s' or other_name = '%s'))
			and media_id IN (SELECT media_id
							FROM Media
							WHERE name = '%s')
		"""%(species, strain, strain, media)
		
		#execute the query
		cursor.execute(query)
		rows=cursor.fetchall()

		#start http return 
		print("Content-type: text/html\n")
		#print the rows of the response
		for row in rows:
			print(row[0], row[1], row[2])

else:
	#no form data, just print an empty http header
	print("Content-type: text/html\n")