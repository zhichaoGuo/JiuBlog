from datetime import datetime

from sqlalchemy import event
from werkzeug.security import generate_password_hash, check_password_hash

from jiublog.extension import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False, comment='user id', autoincrement=True)
    username = db.Column(db.String(40), unique=True, nullable=False, comment='user name')
    email = db.Column(db.String(40), unique=True, nullable=False, comment='user register email')
    password = db.Column(db.String(128), nullable=False, comment='user password')
    avatar = db.Column(db.String(128), nullable=False, comment='user avatar')
    group_id = db.Column(db.INTEGER, db.ForeignKey('group.id'),default=2)
    signup_time = db.Column(db.DateTime, default=datetime.now)
    code = db.Column(db.INTEGER, nullable=False, comment='user avatar')
    register = db.Column(db.BOOLEAN, default=False)
    login_time = db.Column(db.DateTime, default=datetime.now)
    ban = db.Column(db.BOOLEAN, default=False)
    log_off = db.Column(db.BOOLEAN, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def is_ban(self):
        return self.ban

    def is_log_off(self):
        return self.log_off

    def is_register(self):
        return self.register


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False, comment='group id', autoincrement=True)
    name = db.Column(db.String(40), unique=True, nullable=False, comment='group name')


@event.listens_for(Group.__table__, 'after_create')
def init_global(*args, **kwargs):
    group = {1: "admin",
             2: "user"}
    for g in group:
        new_group = Group(id=g, value=group[g])
        db.session.add(new_group)
    db.session.commit()


class Blog(db.Model):
    __tablename__ = 'blog'


class Draft(db.Model):
    __tablename__ = 'draft'


class BlogType(db.Model):
    __tablename__ = 'blog_type'


class FriendLink(db.Model):
    __tablename__ = 'friend_link'


class Photo(db.Model):
    __tablename__ = 'photo'
