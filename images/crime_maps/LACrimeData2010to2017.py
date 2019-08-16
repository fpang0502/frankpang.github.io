
#https://www.opendatanetwork.com/dataset/data.lacity.org/y8tr-7khq <- explanation of how the data is organized

#dependencies 
#Python 3.6.4
#pandas version 0.24.2
#sqlalchemy version 1.3.1
#mysql-connector version 2.1.4

import csv #comes w/ python no need to pip install
import pandas as pd 
import sqlalchemy 

#create df from csv using pandas
df = pd.read_csv('Crime_Data_from_2010_to_Present.csv')

#drop irrelevant data categories
relevantDF = df.drop(['DR Number', 'Date Reported', 'Area ID', 'Area Name',
 			'Reporting District', 'MO Codes','Victim Age', 'Victim Sex', 
 			'Victim Descent', 'Premise Code', 'Premise Description', "Weapon Description", 
 			"Weapon Used Code", "Cross Street"], axis=1)
relevantDF.rename(columns={'Location ': 'Location'}, inplace=True) #no whitespace allowed


# push pandas df to mySQL
#change IP and database_name as needed
database_username = 'root'
database_password = '1597533985315'
database_ip       = 'localhost:3306'
database_name     = 'cs201project'
#connect to mySQL, pool_recycle is the time out time, if u time out try increasing it
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(
	database_username, database_password, database_ip, database_name),
	pool_recycle=3600, pool_size=5).connect()

#upload data 1000 rows at a time
relevantDF.to_sql(con=database_connection, name='CrimeData', if_exists='replace', chunksize=1000)

#prints column names
print(list(relevantDF.columns.values))
#prints first 10 rows as example
print(relevantDF.head(10))
