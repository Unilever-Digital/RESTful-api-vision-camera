from flask import Blueprint,
from app.models.dbmodel import *
from app.controls.control import *

blog = Blueprint("blog", __name__)


@blog.route("vision/pcl/mas140/carton",  methods=["POST", "GET"])
def qltdata_carton_bi():
    cursor = connectionDatabase( database="Vision_Mas140")
    collection = cursor["Table_ResultCarton"]
    json_data = connectionDatabase(collection)
    return json.dumps(json_data)

@blog.route("vision/pcl/mas140/cap",  methods=["POST", "GET"])
def qltdata_carton_bi():
    cursor = connectionDatabase(database="Vision_Mas140")
    collection = cursor["Table_ResultCap"]
    json_data = connectionDatabase(collection)
    return json.dumps(json_data)

@blog.route("vision/pcl/mas140/counter",  methods=["POST", "GET"])
def qltdata_carton_bi():
    cursor = connectionDatabase(database="Vision_Mas140")
    collection = cursor["Table_ResultCounterOfBottles"]
    json_data = connectionDatabase(collection)
    return json.dumps(json_data)

