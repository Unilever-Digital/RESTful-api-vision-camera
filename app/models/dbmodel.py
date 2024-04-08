from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class counterBottle(db.Model):
    ##DateTime	Line	FGsCode	ProductDescription	BottlesTarget	BottlesResult	Status	Reject
    _id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(100), nullable=False)
    line = db.Column(db.Text, nullable=False)
    fgscode = db.Column(db.Text, nullable=False)
    product_description = db.Column(db.Text, nullable=False)
    bottle_target = db.Column(db.Integer, nullable=False)
    bottle_result = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    reject = db.Column(db.String(100), nullable=True)

class carton(db.Model):
    # ID	DateTime	Line	SKUID	ProductName	Barcode	Status	Reject
    _id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(100),nullable=False)
    line = db.Column(db.Text, nullable=False)
    skuid = db.Column(db.String(100), nullable=False)
    product_name = db.Column(db.Text, nullable=False)
    barcode = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    reject = db.Column(db.String(100), nullable=True)
    
    
    
    
