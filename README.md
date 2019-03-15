**Pyodbc List Of Dicts**

	A wraper around PYODBC that returns a list of dictionary in reponce of any query.

	from PyodbcListOfDicts import SQLExec
	lst_of_dicts = SQLExec(query, server, dataBase, commit)
	
	Parameters:
		query (string): 
			SQL query
		server (string): 
			server name or address
		dataBase (string): 
			database name
		commit (bplean): 
			1 if you like a connection.commit()
			0 if you dont like a connection.commit()

			
**Installation:**

	pip install -i https://test.pypi.org/simple/ PyodbcListOfDicts
	
	or
	
	git clone https://github.com/dariyush/PyodbcListOfDicts.git
	cd PyodbcListOfDicts
	pip install .

	
**Examples:**

    from PyodbcListOfDicts import SQLExec

	server, dataBase, commit = 'AMESYD03','SafeEc', 0 
    query = """SELECT TOP 10 * FROM [dbo].[Company]"""  
    lst_of_dicts = SQLExec(query, server, dataBase, commit)
    
    from pandas import DataFrame
    df = DataFrame( lst_of_dicts )

	
**Contacts:**

	Email: dariyush@gmail.com
	git: https://github.com/dariyush/PyodbcListOfDicts
	PyPi: https://test.pypi.org/project/PyodbcListOfDicts/