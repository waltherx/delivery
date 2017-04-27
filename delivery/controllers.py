from flask import Blueprint
from flask import abort
from flask import flash
from flask import session
from flask import request
from flask import jsonify
from flask import render_template
from delivery import app
from delivery import db
from delivery.models import User

delivery = Blueprint('delivery' ,__name__)


@delivery.route('/api/user',methods=['GET'])
def returnAll():
    res = []
    users = User.query.all()
    if users:
        for usr in users:
            res.append({
                'id': usr.id,
                'username': usr.username,
                'email': usr.email,
                'password': usr.password,
                'image': usr.image,
                'create_date': usr.create_date
                })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)

@delivery.route('/api/user', methods=['POST'])
def addUsr():
    json_args = request.get_json()
    username = json_args['username'] if 'username' in request.json else None
    email = json_args['email'] if 'email' in request.json else None
    password = json_args['password'] if 'password' in request.json else None
    image = json_args['image'] if 'image' in request.json else None
    uno = User(username, email, password, image)
    db.session.add(uno)
    db.session.commit()
    return jsonify({'message': 'insert ok :v'})