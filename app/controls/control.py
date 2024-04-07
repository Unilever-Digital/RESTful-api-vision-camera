import pymssql
import pandas as pd

def connectToSqlServer(server, database, username, password):
    try:
        # Establishing the connection
        conn = pymssql.connect(server=server, user=username,
                               password=password, database=database)
        return conn
    except Exception as e:
        print("Error connecting to SQL Server:", e)
        return None


def noSqlTransform(table):
    """tranform Sql table to tree Node json

    Args:
        table (dataframe)): sql table
    """
    json_string = []
    for index, row in table.iterrows():
        json_row = []
        for index2 in len(row):
            json_row.append({" ".join(["feature", index2]): row[index2]})
        json_string.append(json_row)

def tableSqlServerFetch(conn, table_name):
    """_summary_
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)

    
    
        
        