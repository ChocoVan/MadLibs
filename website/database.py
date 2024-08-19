# create database models

from .createApp import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(100))
    person = db.Column(db.String(100))
    object = db.Column(db.String(100))
    color = db.Column(db.String(100))
    adjective = db.Column(db.String(100))
    verb = db.Column(db.String(100))

class Post(db.Model):
    # id for da notes
    id = db.Column(db.Integer, primary_key=True)
    # the madLibs itself
    # supposed to make it so that the user can:
    # - write a paragraph
    # - highlight specific words they want the kids to fill in
    # - and have ai or some shit determine whether the highlighted word is
    #   a verb, adj, or noun
    title = db.Column(db.String(1000))
    data = db.Column(db.String(1000))
    words = db.relationship('Word')