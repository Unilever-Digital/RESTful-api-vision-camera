from flask import (
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
    if request.method == "POST":
        conn = connectToSqlServer("localhost","Vision_Mas140", "sa", "Password.1")
        data = tableSqlServerFetch(conn, "Table_ResultCarton", columns = ["ID"
            ,"DateTime"
            ,"Line"
            ,"SKUID"
            ,"ProductName"
            ,"Barcode"
            ,"Status"
            ,"Reject"])
        return jsonify(data)
    

@blog.route("/qltdata/couterbottle",  methods=["POST", "GET"])
def qltdata_counter_bottle():
    if request.method == "POST":
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
    if request.method == "POST":
        conn = connectToSqlServer("localhost","Vision_Mas140", "sa", "Password.1")
        data = tableSqlServerFetch(conn, "Table_ResultCap",columns = ["DateTime"
            ,"Line"
            ,"FGsCode"
            ,"ProductName"
            ,"Status"])
        return jsonify(data= data)

@blog.route("/qltdata/carton-bi",  methods=["POST", "GET"])
def qltdata_carton_bi():
    if request.method == "POST":
        mongo_conn = connectToMongoDB( database="Vision_Mas140")
        collection = mongo_conn["Table_ResultCarton"]
        
        # Fetch data from MongoDB and transform to JSON
        json_data = tableMongoDBFetch(collection)
        return jsonify({"quality-carton":json_data})
    elif request.method =="GET":
        mongo_conn = connectToMongoDB(database="Vision_Mas140")
        collection = mongo_conn["Table_ResultCarton"]

        # Fetch data from MongoDB and transform to JSON
        json_data = tableMongoDBFetch_100data(collection)
        return jsonify({"quality-carton": json_data})


@blog.route("/qltdata/counter-bottles-bi",  methods=["POST", "GET"])
def qltdata_counter_bottles_bi():
    if request.method == "POST":
        mongo_conn = connectToMongoDB(database="Vision_Mas140")
        collection = mongo_conn["Table_ResultCounterBottles"]

        # Fetch data from MongoDB and transform to JSON
        json_data = tableMongoDBFetch(collection)
        return jsonify({"quality-counter-bottles": json_data})
    elif request.method =="GET":
        mongo_conn = connectToMongoDB(database="Vision_Mas140")
        collection = mongo_conn["Table_ResultCounterBottles"]

        # Fetch data from MongoDB and transform to JSON
        json_data = tableMongoDBFetch_100data(collection)
        return jsonify({"quality-counter-bottles": json_data})


@blog.route("/qltdata/cap-bi",  methods=["POST", "GET"])
def qltdata_cap_bi():
    if request.method == "POST":
        mongo_conn = connectToMongoDB(database="Vision_Mas140")
        collection = mongo_conn["Table_ResultCap"]

        # Fetch data from MongoDB and transform to JSON
        json_data = tableMongoDBFetch(collection)
        return jsonify({"quality-cap": json_data})
    elif request.method =="GET":
        mongo_conn = connectToMongoDB(database="Vision_Mas140")
        collection = mongo_conn["Table_ResultCap"]

        # Fetch data from MongoDB and transform to JSON
        json_data = tableMongoDBFetch_100data(collection)
        return jsonify({"quality-cap": json_data})


@blog.route("/user", methods=["POST", "GET"])
def user():
    return render_template("blog/user.html")
