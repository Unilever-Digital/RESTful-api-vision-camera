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
        data = tableSqlServerFetch(conn, "Table_ResultCarton")
        return jsonify(data)
    

@blog.route("/qltdata/couterbottle",  methods=["POST", "GET"])
def qltdata_counter_bottle():
    if request.method == "GET":
        type = request.values()
        conn = connectToSqlServer("localhost","Vision_Mas140", "sa", "Password.1")
        data = tableSqlServerFetch(conn, "Counter_Bottle")
        return jsonify(data)



@blog.route("/user", methods=["POST", "GET"])
def user():
    return render_template("blog/user.html")
