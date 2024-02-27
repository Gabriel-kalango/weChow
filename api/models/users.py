from ..utils import db
from datetime import datetime
#creating a database model for user creation
class User(db.Model):
    """model for creating dishes"""
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    phone_number=db.Column(db.String(50),nullable=False,unique=True)
    first_name=db.Column(db.String(40),nullable=False)
    last_name=db.Column(db.String(40),nullable=False)
    email=db.Column(db.String(40),nullable=False,unique=True)
    birthday=db.Column(db.String(30),nullable=False)
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit() 

    def delete(self):
        db.session.delete(self)
        db.session.commit()

