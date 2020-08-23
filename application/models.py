import flask
from application import db

class User(db.Document):
    _id         = db.ObjectIdField()
    id          = db.IntField( unique=True )
    first_name  = db.StringField( max_length=50 )
    last_name   = db.StringField( max_length=50 )
    email       = db.StringField(max_length=30)
    password    = db.StringField(max_length=30)

class Course(db.Document):
    _id         = db.ObjectIdField()
    courseID    = db.StringField( max_length=10, unique=True )
    title       = db.StringField( max_length=10 )
    description = db.StringField( max_length=255 )
    credits     = db.IntField()
    term        = db.StringField( max_length=30)

class Enrollment(db.Document):
    course_id   = db.StringField()
    id          = db.StringField()
