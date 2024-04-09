import pyodbc
import json
import pymongo

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
    
def connectToMongoDB(database):
    try:
        uri = "mongodb+srv://unilever-digital:U2024-digital@cluster0.ixcliyp.mongodb.net/"
        # Establishing the connection
        conn = pymongo.MongoClient(uri)
        return conn[database]
    except Exception as e:
        print("Error connecting to MongoDB:", e)
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


def tableMongoDBFetch(collection, query=None, projection=None):
    """
    Fetch data from a MongoDB collection and convert it to JSON format.

    Args:
        collection (pymongo.collection.Collection): Collection object from which to fetch data.
        query (dict): Query to filter documents (optional).
        projection (dict): Projection to include/exclude fields in the result (optional).

    Returns:
        str: JSON representation of the fetched data.

    Raises:
        Exception: If an error occurs during the execution.
    """
    try:
        # Fetch documents from the collection
        if query is None:
            query = {}
        if projection is None:
            projection = {}

        cursor = collection.find(query, projection)
        rows = list(cursor)

        # Remove _id field from each document
        for doc in rows:
            doc.pop('_id', None)

        # Convert the list of dictionaries to JSON
        return rows
    except Exception as e:
        print(e)
        raise


def tableMongoDBFetch_100data(collection, query=None, projection=None):
    """
    Fetch 100 rows of data from a MongoDB collection and convert it to JSON format.

    Args:
        collection (pymongo.collection.Collection): Collection object from which to fetch data.
        query (dict): Query to filter documents (optional).
        projection (dict): Projection to include/exclude fields in the result (optional).

    Returns:
        str: JSON representation of the fetched data.

    Raises:
        Exception: If an error occurs during the execution.
    """
    try:
        # Fetch documents from the collection
        if query is None:
            query = {}
        if projection is None:
            projection = {}

        cursor = collection.find(query, projection).limit(
            100)  # Limit to 100 rows
        rows = list(cursor)

        # Remove _id field from each document
        for doc in rows:
            doc.pop('_id', None)

        # Convert the list of dictionaries to JSON
        return rows
    except Exception as e:
        print(e)
        raise


