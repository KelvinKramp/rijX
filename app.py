from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import current_user, Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
import os
import json
from dotenv import load_dotenv

load_dotenv()

# MAKE DIFFERENCE BETWEEN PRODUCTION AND DEVELOPMENT ENVIRONMENT
if "Users" in os.getcwd():
    SQL_URI = 'sqlite:///app.sqlite3'
else:
    SQL_URI = os.environ['DATABASE_URL']
    if SQL_URI and SQL_URI.startswith("postgres://"):
        SQL_URI = SQL_URI.replace("postgres://", "postgresql://", 1)


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config ['SQLALCHEMY_DATABASE_URI'] = SQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# code source https://ckraczkowsky.medium.com/building-a-secure-admin-interface-with-flask-admin-and-flask-security-13ae81faa05

# Instantiate the Flask application with configurations
secureApp = app
# Configure a specific Bootswatch theme
secureApp.config['FLASK_ADMIN_SWATCH'] = 'sandstone'
secureApp.config['SECRET_KEY'] = os.environ['SECRET_KEY_ADMIN']
secureApp.config['SECURITY_PASSWORD_SALT'] = os.environ['SECURITY_PASSWORD_SALT']
# Configure application to route to the Flask-Admin index view upon login
secureApp.config['SECURITY_POST_LOGIN_VIEW'] = '/admin/'
# Configure application to route to the Flask-Admin index view upon logout
secureApp.config['SECURITY_POST_LOGOUT_VIEW'] = '/admin/'
# Configure application to route to the Flask-Admin index view upon registering
secureApp.config['SECURITY_POST_REGISTER_VIEW'] = '/admin/'
secureApp.config['SECURITY_REGISTERABLE'] = False
# Configure application to not send an email upon registration
secureApp.config['SECURITY_SEND_REGISTER_EMAIL'] = False
secureApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate the database
db = SQLAlchemy(secureApp)

# Create a table of users and user roles
roles_users_table = db.Table('roles_users',
                            db.Column('users_id', db.Integer(), db.ForeignKey('users.id')),
                            db.Column('roles_id', db.Integer(), db.ForeignKey('roles.id')))

class Users(db.Model, UserMixin):
    # Users class inheritis properties like is_active and is_authenticated from UserMixin
    # By inheriting from UserMixin, safety measures that Flask implements are being inherited
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())
    roles = db.relationship('Roles', secondary=roles_users_table, backref='user', lazy=True)

# Define models for the users and user roles
class Roles(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Appointments(db.Model):
    # use long strings for db storage to facilitate encrypted strings
    __tablename__ = 'Appointments'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(300), unique=False, nullable=False)
    datetime = db.Column(db.String(20), unique=False, nullable=False)
    first_name = db.Column(db.String(200), unique=False, nullable=False)
    last_name = db.Column(db.String(200), unique=False, nullable=False)
    birthdate = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(200), unique=False, nullable=False)
    phone_number = db.Column(db.String(200), unique=False, nullable=False)
    time = db.Column(db.String(100), unique=False, nullable=True)

    def __init__(self, location, datetime, first_name, last_name, birthdate, email, phone_number, time):
        self.location = location
        self.datetime = datetime
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.email = email
        self.phone_number = phone_number
        self.time = time

class Slots(db.Model):
    __tablename__ = 'Slots'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(300), unique=False, nullable=False)
    date = db.Column(db.Date(), unique=False, nullable=False)
    starttime = db.Column(db.Time(), unique=False, nullable=False)
    endtime = db.Column(db.Time(), unique=False, nullable=False)
    timeduration = db.Column(db.String(200), unique=False, nullable=False)
    worker = db.Column(db.String(50), unique=False, nullable=False)
    BIG = db.Column(db.BigInteger, unique=False, nullable=False)
    group_id = db.Column(db.Integer, nullable=True)

    def __init__(self, location, date, starttime, endtime, timeduration, worker, BIG, group_id):
        self.location = location
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.timeduration = timeduration
        self.worker = worker
        self.BIG = BIG
        self.group_id = group_id

# connect this class to id worker from Slots class later
class Workers(db.Model):
    __tablename__ = 'Workers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    BIG = db.Column(db.String(20), unique=True, nullable=False)
    openslots = db.Column(db.String(20), unique=False, nullable=False)

    def __init__(self, name, BIG, openslots):
        self.name = name
        self.BIG = BIG
        self.openslots = openslots

if __name__ == '__main__':
    # data = Workers("qwasdaeqe","easdasdr","Qwasdae")
    # db.session.add(data)
    # db.session.commit()
    # l = Workers.query.all()
    # print(l)
    db.create_all()