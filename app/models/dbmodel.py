from app import app
from app import db

class counterBottle(db.Model):
    ##DateTime	Line	FGsCode	ProductDescription	BottlesTarget	BottlesResult	Status	Reject
    _id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(100), nullable=False)
    line = db.Column(db.Text, nullable=False)
    fgscode = db.Columns(db.Text, nullable=False)
    product_description = db.Columns(db.Text, nullable=False)
    bottle_target = db.Columns(db.Integer, nullable=False)
    bottle_result = db.Columns(db.Integer, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    reject = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Post(title='{self.title}', content='{self.content}')"

class barcodeBottle(db.Model):
    # ID	DateTime	Line	SKUID	ProductName	Barcode	Status	Reject
    _id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(100),nullable=False)
    line = db.Column(db.Text, nullable=False)
    skuid = db.Column(db.String(100), nullable=False)
    product_name = db.Column(db.Text, nullable=False)
    barcode = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    reject = db.Column(db.String(100), nullable=False)
    
    
    
    
