import pytest
from app import create_app

app = create_app()

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


# Index link test connection
def test_pcl_mas140_carton(client):
    response = client.get('/vision/pcl/mas140/carton')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_pcl_mas140_cap(client):
    response = client.get('/vision/pcl/mas140/cap')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_pcl_mas140_counter(client):
    response = client.get('/vision/pcl/mas140/counter')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_pouch_imagefail(client):
    response = client.get('/vision/hcl/pouch/imagefail')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_pouch_checkweight(client):
    response = client.get('/vision/hcl/pouch/checkweight')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_pouch_dataman(client):
    response = client.get('/vision/hcl/pouch/dataman')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_pouch_carton(client):
    response = client.get('/vision/hcl/pouch/carton')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_stn_barcode(client):
    response = client.get('/vision/hcl/stn/barcode')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_stn_barcode(client):
    response = client.get('/vision/hcl/stn/barcode')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_stn_cap1(client):
    response = client.get('/vision/hcl/stn/cap1')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_stn_cap2(client):
    response = client.get('/vision/hcl/stn/cap2')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_stn_lo1(client):
    response = client.get('/vision/hcl/stn/lo1')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_stn_lo2(client):
    response = client.get('/vision/hcl/stn/lo2')
    html_data = response.data.decode('utf-8')
    return html_data[0]

def test_hcl_stn_datecode(client):
    response = client.get('/vision/hcl/stn/datecode')
    html_data = response.data.decode('utf-8')
    return html_data[0]
