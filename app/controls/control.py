import pyodbc
import pandas as pd
import json

def connectToSqlServer(server, database, username, password):
    try:
        # Establishing the connection
        conn = pyodbc.connect(driver = "ODBC Driver 17 for SQL Server", 
                              server=server, 
                              user=username,
                              password=password, 
                              database=database,
                              port= 1433)
        return conn
    except Exception as e:
        print("Error connecting to SQL Server:", e)
        return None


def noSqlTransform(rows):
    """tranform Sql table to tree Node json

    Args:
        table (dataframe)): sql table
    """
    try:
    
        # Convert rows to a list of dictionaries
        results = []
        for row in rows:
            results.append(dict(row))

        # Convert the list of dictionaries to JSON
        return json.dumps(results)
    except Exception as e:
        print(e)

def tableSqlServerFetch(conn, table_name, columns):
    """_summary_
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        # Convert rows to a list of dictionaries
        results = []
        for row in rows:
            results.append([dict(col,str(x)) for x, col in zip(row, columns)])

        # Convert the list of dictionaries to JSON
        return json.dumps(results, indent=4)
    except Exception as e:
        print(e)

    
    
        
        