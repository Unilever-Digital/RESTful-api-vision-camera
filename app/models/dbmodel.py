from app import app
from app import db

class counterBottle(db.Model):
    ##DateTime	Line	FGsCode	ProductDescription	BottlesTarget	BottlesResult	Status	Reject
    _id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(100), nullable=False)
    line = db.Column(db.Text, nullable=False)
    fgscode = db.Columns()
    

    def __repr__(self):
        return f"Post(title='{self.title}', content='{self.content}')"

class barcodeBottle(db.Model):
    # ID	DateTime	Line	SKUID	ProductName	Barcode	Status	Reject
    _id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(100),nullable=False)
    
    
