from datetime import datetime, timedelta

from flask import render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

from blog import app
from blog.database import db_session as dao
from blog.models.post import Post
from blog.models.comment import Comment

@app.route('/', methods=['GET'])
def index():
    posts = dao.query(Post).options(joinedload(Post.comments)).order_by(Post.created_at.desc()).all()[:3]
    # cause N+1 query
    # http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html 이걸 참고해서 고쳐봅시다
    return render_template('index.html', posts=posts)

# http://flask.pocoo.org/docs/0.12/templating/#context-processors
@app.context_processor
def sidebar_processor():
    def recent_posts():
        posts = dao.query(Post).order_by(Post.created_at.desc()).all()[:5]
        return posts
    def recent_comments():
        comments = dao.query(Comment).options(joinedload(Comment.post, innerjoin=True)).order_by(Comment.created_at.desc()).all()[:5]
        return comments
    return dict(recent_posts=recent_posts(), recent_comments=recent_comments())

# http://jinja.pocoo.org/docs/2.9/templates/#filters
# http://jinja.pocoo.org/docs/2.9/api/#custom-filters
# http://flask.pocoo.org/docs/0.12/templating/#registering-filters

# this from http://flask.pocoo.org/snippets/33/
@app.template_filter('rel_dateformat')
def timesince(dt, default="just now"):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """

    now = datetime.utcnow()
    diff = now - dt

    periods = (
        (diff.days / 365, "년"),
        (diff.days / 30, "개월"),
        (diff.days / 7, "주"),
        (diff.days, "일"),
        (diff.seconds / 3600, "시간"),
        (diff.seconds / 60, "분"),
        (diff.seconds, "초"),
    )

    for period, unit in periods:
        if period >= 1:
            return "%d%s 전" % (period, unit)

    return default
