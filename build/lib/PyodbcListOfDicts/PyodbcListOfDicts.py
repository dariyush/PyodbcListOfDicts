# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:52:34 2019

@author: a.mohammadi
"""

import pyodbc
from collections import OrderedDict

#%%
def GetConnection(server, database):
    return pyodbc.connect( ''.join(
                [r'DRIVER={ODBC Driver 13 for SQL Server};',
                 r'Trusted_Connection=yes;',
                 r'SERVER=%s;' %server,
                 r'DATABASE=%s;' %database,]) )
    
def SQLExec(query, server, dataBase, commit):
    with GetConnection(server,dataBase) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            description = cursor.description #[col[0] for col in cursor.description]
            if commit:
                connection.commit()
    
    lst = []
    for row in rows:
        d = OrderedDict()
        for k, v in zip( description, row ):
            d[k[0]] = v
        lst.append( d )
    
    return lst
    # return [{k[0]: v for k, v in zip( description, row )} for row in rows]            

#%%
if __name__ == "__main__":
    server, dataBase, commit = 'AMESYD03','SafeEc', 0 
    query = """SELECT TOP 10 * FROM [dbo].[Company]"""  
    
    lst_of_dicts = SQLExec(query, server, dataBase, commit)
    
    from pandas import DataFrame
    df = DataFrame( lst_of_dicts )