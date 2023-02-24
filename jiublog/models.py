from jiublog.extension import db


class User(db.Model):
    __tablename__ = 'user'


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
