import datetime
import json
from delivery import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(70))
    password = db.Column(db.String(70))
    image = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default= datetime.datetime.now)

    def __init__(self ,username , email, password, image):
        self.username = username
        self.email = email
        self.password = self.__create_password(password)
        self.image = image

    def __create_password(self, passw):
        return generate_password_hash(passw)

    def verify_password(self, passw):
        return check_password_hash(self.password, passw)
