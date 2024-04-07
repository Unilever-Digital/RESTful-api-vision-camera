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


@blog.route("/qltdata",  methods=["POST", "GET"])
def home():
    if request.method == "POST":
        type = request.values()
        conn = connectToSqlServer("localhost", "quality", "sa", "1")
        data = tableSqlServerFetch(conn, type)
        return jsonify(noSqlTransform(data))


@blog.route("/user", methods=["POST", "GET"])
def user():
    return render_template("blog/user.html")
