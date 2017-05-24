from django.shortcuts import render
from django.http import HttpResponse
import pyodbc

# Settings
server = 'tcp:HS-SPADES-01' 
database = 'CosmosData' 
username = 'Hackday' 
password = 'Hackday' 

def get_influence_score(request, name, id):
	# Establish db connection
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	# query db for the user's influence score.
	query = "SELECT * FROM UserInfluenceScores WHERE Puid = '" + id + "' FOR JSON PATH;"
	cursor.execute(query)
	row = cursor.fetchone()
	response = '';
	while row:
		response += row[0]
		row = cursor.fetchone()
	return '{"data":' + response + '}'