from flask import render_template, request, redirect, url_for

from blog import app
from blog.database import db_session as dao
from blog.models.post import Post
from blog.models.comment import Comment

@app.route('/', methods=['GET'])
def index():
    posts = dao.query(Post).order_by(Post.created_at.desc()).all()[:3]
    # cause N+1 query
    return render_template('index.html', posts=posts)
