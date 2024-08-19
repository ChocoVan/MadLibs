# use get method to retrieve posts
# users can see madlib paragraphs on this page
# can edit posts here as well

from flask import Blueprint, render_template, flash, request, url_for, jsonify
from .database import Post
from .createApp import db
import json

readPost = Blueprint('readPost', __name__)

@readPost.route('/madlibs', methods=['GET', 'POST'])
def get_post():
    posts = Post.query.all()
    return render_template("getPost.html", posts=posts)

@readPost.route('/madlibs/delete-post', methods=['POST'])
def delete_post():

    post_to_delete = json.loads(request.data)
    noteId = post_to_delete['noteId']
    post_to_delete = Post.query.get(noteId)
    # post_to_delete = Post.query.all()

    if post_to_delete:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Post has been deleted!', category='success')

    posts = Post.query.all()
    #return render_template("getPost.html", posts=posts)

    #note = json.loads(request.data)
    #noteId = note['noteId']
    #note = Post.query.get(noteId)
    #db.session.delete(note)
    #db.session.commit()

    return jsonify({})

