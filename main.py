from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS, cross_origin
from sqlalchemy import func


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///task.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50),  nullable=False)
    l_name = db.Column(db.String(50),  nullable=False)
    email = db.Column(db.String(150), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10),  nullable=False)
    education = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    Experience = db.Column(db.Integer, nullable=True)
    package = db.Column(db.Integer, nullable=False)
    
@app.route('/')
def test():
    return 'this is test'

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    return response

@app.route('/user', methods=['POST'])
def new_user():
    data = request.get_json()
    new_user=User(f_name=data['firstName'],l_name=data['lastName'],email=data['email'],dob=data['dob'],gender=data['gender'],education=data['education'],company=data['company'],Experience=data['experience'],package=data['package'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'success': True}), 200


@app.route('/get_user')
def getuser():
    new_users=User.query.all()
    output = []
    for new_user in new_users:
        user_data = {}
        user_data['id'] = new_user.id
        user_data['firstName'] = new_user.f_name
        user_data['lastName'] = new_user.l_name
        user_data['email'] = new_user.email
        user_data['dob'] = new_user.dob
        user_data['gender'] = new_user.gender
        user_data['education'] = new_user.education
        user_data['company'] = new_user.company
        user_data['experience'] = new_user.Experience
        user_data['package'] = new_user.package
        output.append(user_data)
    return jsonify( output)


@app.route('/delete_user/<id>', methods=['DELETE'])
def deleteuser(id):
    user =User.query.filter_by(id=id).first()

    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': True}), 200


@app.route('/update_user/<id>', methods=['PUT'])
def updateuser(id):
    data = request.get_json()
    user =User.query.filter_by(id=id).first()

    user.f_name = data['firstName']
    user.l_name= data['lastName']
    user.email= data['email']
    user.dob=data['dob']
    user.gender=data['gender']
    user.education=data['education']
    user.company=data['company']
    user.Experience=data['experience']
    user.package=data['package']
    db.session.add(user)
    db.session.commit()
    return jsonify({'success': True}), 200

with app.app_context():
    db.create_all()

app.run(debug=True, port=5555)
