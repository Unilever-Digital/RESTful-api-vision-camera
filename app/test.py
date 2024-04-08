import pandas as pd
import pyodbc

if __name__ == "__main__":
    # Read Excel data into a DataFrame
    column_names = ['ID', 'DateTime', 'Line', 'SKUID', 'ProductName', 'Barcode', 'Status', 'Reject']

    # Read Excel data into a DataFrame with specified column names
    excel_file = 'data.xlsx'
    df = pd.read_excel(excel_file, names=column_names)
    connection = pyodbc.connect(driver="ODBC Driver 17 for SQL Server",
        server='localhost',
        database='Vision_Mas140',
        uid='sa',  # Replace with your username
        pwd='Password.1',  # Replace with your password
        port=1433)   
    cursor = connection.cursor()
    for index, row in df.iterrows():
        # Construct the SQL INSERT statement
        sql = "INSERT INTO Table_ResultCarton (ID, DateTime, Line, SKUID, ProductName, Barcode, Status, Reject) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        values = (str(row['ID']), row['DateTime'], row['Line'], str(row['SKUID']),
              row['ProductName'], str(row['Barcode']), row['Status'], row['Reject'])
        print(values)

        # Execute the SQL statement
        cursor.execute(sql, values)

    # Commit the transaction (save changes to the database)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
