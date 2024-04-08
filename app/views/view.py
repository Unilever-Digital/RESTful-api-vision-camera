from flask import (
    Flask,
    Blueprint,
    render_template,
    request,
    jsonify
)
from app.models.dbmodel import *
from app.controls.control import *



blog = Blueprint("blog", __name__)


@blog.route("/qltdata/carton",  methods=["POST", "GET"])
def qltdata_carton():
    if request.method == "GET":
        conn = connectToSqlServer("localhost","Vision_Mas140", "sa", "Password.1")
        data = tableSqlServerFetch(conn, "Table_ResultCarton", columns = ["ID"
            ,"DateTime"
            ,"Line"
            ,"SKUID"
            ,"ProductName"
            ,"Barcode"
            ,"Status"
            ,"Reject"])
        
        # Specify the file path
        file_path = "data.json"

        # Open the file in write mode
        with open(file_path, "w") as file:
            # Write JSON data to the file
            file.write(data)
        return jsonify(data)
    

@blog.route("/qltdata/couterbottle",  methods=["POST", "GET"])
def qltdata_counter_bottle():
    if request.method == "GET":
        type = request.values()
        conn = connectToSqlServer("localhost","Vision_Mas140", "sa", "Password.1")
        data = tableSqlServerFetch(conn, "Table_ResultCounterBottles",columns = ["DateTime"
            ,"Line"
            ,"FGsCode"
            ,"ProductName"
            ,"Result"
            ,"Status"])
        return jsonify(data)
        
@blog.route("/qltdata/cap",  methods=["POST", "GET"])
def qltdata_cap():
    if request.method == "GET":
        type = request.values()
        conn = connectToSqlServer("localhost","Vision_Mas140", "sa", "Password.1")
        data = tableSqlServerFetch(conn, "Table_ResultCap",columns = ["DateTime"
            ,"Line"
            ,"FGsCode"
            ,"ProductName"
            ,"Status"])
        return jsonify(data)


@blog.route("/qltdata/carton-bi",  methods=["POST", "GET"])
def qltdata_carton_bi():
    mongo_conn = connectToMongoDB( database="Vision_Mas140")
    collection = mongo_conn["Table_ResultCarton"]
    # Fetch data from MongoDB and transform to JSON
    json_data = tableMongoDBFetch(collection)
    return json_data


@blog.route("/qltdata/counter-botton-bi",  methods=["POST", "GET"])
def qltdata_counter_bottles_bi():
    mongo_conn = connectToMongoDB(database="Vision_Mas140")
    collection = mongo_conn["Table_ResultCounterBottles"]

    # Fetch data from MongoDB and transform to JSON
    json_data = tableMongoDBFetch(collection)
    return json_data


@blog.route("/qltdata/cap-bi",  methods=["POST", "GET"])
def qltdata_cap_bi():
    mongo_conn = connectToMongoDB(database="Vision_Mas140")
    collection = mongo_conn["Table_ResultCap"]

    # Fetch data from MongoDB and transform to JSON
    json_data = tableMongoDBFetch(collection)
    return json_data


@blog.route("/user", methods=["POST", "GET"])
def user():
    return render_template("blog/user.html")
