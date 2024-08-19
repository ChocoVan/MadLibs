from flask import Blueprint, render_template, flash, request
from .database import Post
from .createApp import db
from flask import json

create = Blueprint('create', __name__)

@create.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        t = request.form.get('title')
        post = request.form.get('post')

        if len(post) < 1:
            flash('Note is too short!', category='error')
        else:
            new_post = Post(title=t, data=post)
            db.session.add(new_post)
            db.session.commit()
            flash('Finished with the first step!', category='success')

    return render_template("createPost.html")

@create.route('/create/choose', methods=['GET', 'POST'])
def choose_words():
    post_to_choose = json.loads(request.data)
    postId = post_to_choose['postId']
    post_to_choose = Post.query.get(postId)

    return render_template("chooseWords.html")

# highlight words while creating post
# highlighted words will be converted to either "noun", "verb", "adjective", etc.
# then they will be shown on the right