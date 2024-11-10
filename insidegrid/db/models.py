from datetime import datetime

from sqlalchemy import VARCHAR, Column, Integer, DateTime, ForeignKey, Text, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import ARRAY

from insidegrid.db import Base
from insidegrid.consts import CHANGE_STATUS

class Users(Base):
    __tablename__ = "users"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', VARCHAR(length=30), unique=True, nullable=False)
    account_email = Column('user_email', VARCHAR(length=250), unique=True)
    password = Column('user_password', VARCHAR(length=16), nullable=False)
    role = Column('role', VARCHAR(length=40), nullable=False)


class Changes(Base):
    __tablename__ = "changes"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, unique=True, nullable=False)
    status = Column('status', VARCHAR(100), server_default=CHANGE_STATUS.requested.value, default=CHANGE_STATUS.requested.value)
    creator_user_id = Column(ForeignKey(Users.id))
    description = Column('description', Text, nullable=False)
    parent_id = Column('parrent_id', Integer, ForeignKey('changes.id'))
    tags = Column('tags', ARRAY(String), nullable=True)

class Releases(Base):
    __tablename__ = "releases"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, unique=True, nullable=False)
    change_id = Column(ForeignKey(Changes.id))
    description = Column('description', Text, nullable=False)
    release_date = Column('release_date', DateTime, nullable=False)
    release_source = Column('release_source', String, nullable=False) #urls
    release_documents = Column('release_documents', ARRAY(String)) #array of links to files
    type = Column('type', String, nullable=False)
    tags = Column('tags', ARRAY(String), nullable=True)

class LikedChanges(Base):
    __tablename__ = "liked_changes"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(Users.id))
    change_id = Column(ForeignKey(Changes.id))

class DislikedChanges(Base):
    __tablename__ = "disliked_changes"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(Users.id))
    change_id = Column(ForeignKey(Changes.id))

class Subscriptions(Base):
    __tablename__ = "subscriptions"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(Users.id))
    change_id = Column(ForeignKey(Changes.id))


class LikedReleases(Base):
    __tablename__ = "liked_releases"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(Users.id))
    release_id = Column(ForeignKey(Releases.id))

class DislikedReleases(Base):
    __tablename__ = "disliked_releases"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(Users.id))
    release_id = Column(ForeignKey(Releases.id))

class Comments(Base):
    __tablename__ = "comments"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    change_id = Column(ForeignKey(Changes.id), nullable=True)
    release_id = Column(ForeignKey(Releases.id), nullable=True)
    author_id = Column(ForeignKey(Users.id))
    content = Column('content', Text, nullable=False)
    date = Column('date', DateTime, nullable=False)
    replied_to_comment_id = Column(ForeignKey('comments.id'), nullable=True)
    likes = Column('likes', Integer, nullable=False, default=0)
    dislikes = Column('dislikes', Integer, nullable=False, default=0)
