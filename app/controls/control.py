import json
import pymongo
    
def connectionDatabase(database):
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

def fetchCursorDatabase(collection, query=None, projection=None):
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
        if query is None:
            query = {}
        if projection is None:
            projection = {}
            
        cursor = collection.find(query, projection)
        rows = list(cursor)
        for doc in rows:
            doc.pop('_id', None)
        return rows
    except Exception as e:
        print(e)
        raise