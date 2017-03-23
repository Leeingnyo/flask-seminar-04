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

# http://flask.pocoo.org/docs/0.12/templating/#context-processors
@app.context_processor
def sidebar_processor():
    def recent_posts():
        posts = dao.query(Post).order_by(Post.created_at.desc()).all()[:5]
        return posts
    def recent_comments():
        comments = dao.query(Comment).order_by(Comment.created_at.desc()).all()[:5]
        return comments
    return dict(recent_posts=recent_posts(), recent_comments=recent_comments())
