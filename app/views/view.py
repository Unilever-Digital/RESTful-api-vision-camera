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
    if request.method == "POST":
        type = request.values()
        conn = connectToSqlServer("localhost", "quality", "sa", "Password1")
        data = tableSqlServerFetch(conn, "carton")
        return jsonify(noSqlTransform(data))
    

@blog.route("/qltdata/couterbottle",  methods=["POST", "GET"])
def qltdata_counter_bottle():
    if request.method == "POST":
        type = request.values()
        conn = connectToSqlServer("localhost", "quality", "sa", "Password1")
        data = tableSqlServerFetch(conn, "Counter_Bottle")
        return jsonify(noSqlTransform(data))



@blog.route("/user", methods=["POST", "GET"])
def user():
    return render_template("blog/user.html")
