from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#mysql://root:toor@localhost/delivery

#  postgresql://postgres:toor@localhost/delivery
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:toor@localhost/delivery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from delivery.controllers import delivery
app.register_blueprint(delivery)

db.create_all()