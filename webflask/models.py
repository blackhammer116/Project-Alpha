from datetime import datetime
from flask_login import UserMixin
from webflask import db

test_request_service = db.Table(
    'test_request_service',
    db.Column('request_id', db.Integer,
              db.ForeignKey('test_request.request_id', ondelete='CASCADE')),
    db.Column('service_id', db.Integer, db.ForeignKey('service.service_id', ondelete='CASCADE'))
)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(255))
    # New field for admin status
    is_admin = db.Column(db.Boolean, default=False)
    notes = db.relationship('Note')
    test_requests = db.relationship('TestRequest')


class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'))


class TestRequest(db.Model):
    __tablename__ = 'test_request'
    request_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    ip = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    services = db.relationship(
        'Service', secondary=test_request_service, backref='test_requests')


class Service(db.Model):
    __tablename__ = 'service'
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
