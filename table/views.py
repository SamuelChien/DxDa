from django.shortcuts import render
from django.http import HttpResponse
import pyodbc

# Settings
server = 'tcp:HS-SPADES-01' 
database = 'CosmosData' 
username = 'Hackday' 
password = 'Hackday' 

# Create your views here.
def index(request):
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()

	cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';")
	rtn = ""
	row = cursor.fetchone()
	while row: 
		rtn += str(row) + "<br>\n"
		row = cursor.fetchone() 

	return HttpResponse(rtn)
	
def table(request, name, column=None, value=None):
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()

	type = request.GET.get('type', '')
	sort = request.GET.get('sort', '')
	order = request.GET.get('order', 'ASC')
	top = request.GET.get('top', '15000')
	if len(sort)>2:
		sort = " ORDER BY " + sort + " " + order
	
#	cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';")
	if column is not None and value is not None:
		query = "SELECT TOP " + top + "* FROM " + name + " WHERE " + column + "='" + value + "'" + sort + " FOR JSON PATH;"
	else:	
		query = "SELECT TOP " + top + " * FROM " + name + sort + " FOR JSON PATH;"
	
	cursor.execute(query)
	row = cursor.fetchone()
	rtn = ""
	while row:
		rtn += row[0]
		row = cursor.fetchone()
	
	if type=='nvd3':
		rtn = '[{"values":' + rtn + '}]'
	elif type=="datatables":
		rtn = '{"data":' + rtn + '}'
    
	return HttpResponse(rtn, content_type="application/json")

def select(request, query):
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()

	cursor.execute(query)

	type = request.GET.get('type', '')

	row = cursor.fetchone()
	rtn = ""
	while row:
		if (len(row)==1):
			rtn += row[0]
		else:
			rtn += str(row) + "\n"
		row = cursor.fetchone()

	if type=='nvd3':
		rtn = '[{"values":' + rtn + '}]'
	elif type=="datatables":
		rtn = '{"data":' + rtn + '}'
    
	return HttpResponse(rtn, content_type="application/json")

	
def my_network(request, name, id):
	response = '';
	if name.lower() == 'influence' : 
		response = get_influence_score(request, name, id)
	elif name.lower() == 'coauthors' :
		response = 'Get coauthors for id: ' + id
	else :
		response = 'Invalid request: ' + name 
	
	return HttpResponse(response, content_type="application/json")
	
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
		response += str(row[0])
		row = cursor.fetchone()
	return '{"data":' + response + '}'	

	