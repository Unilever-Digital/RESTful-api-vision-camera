from flask import Blueprint
from app.models.dbmodel import *
from app.controls.control import *

blog = Blueprint("blog", __name__)

#PCL vision camera restfulapi-----------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
#mas140
@blog.route("/vision/pcl/mas140/carton")
def vision_pcl_mas140_carton():
    """_summary_

    Returns:
        _json_: _root data json of mas140 carton vision cam bi_
    """
    try:
        cursor = connectionDatabase("Vision_Mas140")
        collection = cursor["Table_ResultCarton"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

@blog.route("/vision/pcl/mas140/cap", methods=["POST", "GET"])
def vision_pcl_mas140_cap():
    """_summary_

    Returns:
        _json_: _root data json of mas140 cap vision cam bi_
    """
    try:
        cursor = connectionDatabase("Vision_Mas140")
        collection = cursor["Table_ResultCap"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

@blog.route("/vision/pcl/mas140/counter", methods=["POST", "GET"])
def vision_pcl_mas140_counter():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam bi_
    """
    try:
        cursor = connectionDatabase("Vision_Mas140")
        collection = cursor["Table_ResultCounterBottles"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

#HCL vision cameara restfulapi ---------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
#line Po2
@blog.route("/vision/hcl/po2/imagefail", methods=["POST", "GET"])
def vision_hcl_po2_imagefail():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam STN LO2_
    """
    try:    
        cursor = connectionDatabase("U-CheckDate-Barcode-Po2")
        collection = cursor["Table_ImageFail"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e
    
@blog.route("/vision/hcl/po2/checkweight", methods=["POST", "GET"])
def vision_hcl_po2_checkweight():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam STN LO2_
    """
    try:    
        cursor = connectionDatabase("U-CheckDate-Barcode-Po2")
        collection = cursor["Table_Checkweigher"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

@blog.route("/vision/hcl/po2/dataman", methods=["POST", "GET"])
def vision_hcl_po2_dataman():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam STN LO2_
    """
    try:    
        cursor = connectionDatabase("U-CheckDate-Barcode-Po2")
        collection = cursor["Table_ResultDataman"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e
    
@blog.route("/vision/hcl/po2/carton", methods=["POST", "GET"])
def vision_hcl_po2_carton():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam STN LO2_
    """
    try:    
        cursor = connectionDatabase("U-CheckDate-Barcode-Po2")
        collection = cursor["Table_ResultCarton"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

#line stn
@blog.route("/vision/hcl/stn/barcode", methods=["POST", "GET"])
def vision_hcl_stn_barcode():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam bi_
    """
    try:    
        cursor = connectionDatabase("Stn")
        collection = cursor["Table_ImageFail_Barcode"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

@blog.route("/vision/hcl/stn/cap1", methods=["POST", "GET"])
def vision_hcl_stn_cap1():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam bi_
    """
    try:    
        cursor = connectionDatabase("Stn")
        collection = cursor["Table_ImageFail_Cap1"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

@blog.route("/vision/hcl/stn/cap2", methods=["POST", "GET"])
def vision_hcl_stn_cap2():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam bi_
    """
    try:    
        cursor = connectionDatabase("Stn")
        collection = cursor["Table_ImageFail_Cap2"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e

@blog.route("/vision/hcl/stn/datecode", methods=["POST", "GET"])
def vision_hcl_stn_datecode():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam bi_
    """
    try:    
        cursor = connectionDatabase("Stn")
        collection = cursor["Table_ImageFail_DateCode"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e
    
@blog.route("/vision/hcl/stn/lo1", methods=["POST", "GET"])
def vision_hcl_stn_lo1():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam bi_
    """
    try:    
        cursor = connectionDatabase("Stn")
        collection = cursor["Table_ImageFail_LO1"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e
    
@blog.route("/vision/hcl/stn/lo2", methods=["POST", "GET"])
def vision_hcl_stn_lo2():
    """_summary_

    Returns:
        _json_: _root data json of mas140 counter vision cam STN LO2_
    """
    try:    
        cursor = connectionDatabase("Stn")
        collection = cursor["Table_ImageFail_LO2"]
        json_data = fetchCursorDatabase(collection)
        return json_data
    except Exception as e:
        return e
