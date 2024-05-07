from flask import Blueprint
from app.models.dbmodel import *
from app.controls.control import *

blog = Blueprint("blog", __name__)


@blog.route("/vision/pcl/mas140/carton", methods=["POST", "GET"])
def vision_pcl_mas140_carton():
    cursor = connectionDatabase(database="Vision_Mas140")
    collection = cursor["Table_ResultCarton"]
    json_data = fetchCursorDatabase(collection)
    return json.dumps(json_data)

@blog.route("/vision/pcl/mas140/cap", methods=["POST", "GET"])
def vision_pcl_mas140_cap():
    cursor = connectionDatabase(database="Vision_Mas140")
    collection = cursor["Table_ResultCap"]
    json_data = fetchCursorDatabase(collection)
    return json.dumps(json_data)

@blog.route("/vision/pcl/mas140/counter", methods=["POST", "GET"])
def vision_pcl_mas140_counter():
    cursor = connectionDatabase(database="Vision_Mas140")
    collection = cursor["Table_ResultCounterBottles"]
    json_data = fetchCursorDatabase(collection)
    return json.dumps(json_data)

