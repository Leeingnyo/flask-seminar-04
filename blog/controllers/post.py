from datetime import datetime, timedelta

from flask import render_template, request, redirect, url_for, abort
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from blog import app
from blog.database import db_session as dao
from blog.models.post import Post
from blog.models.comment import Comment

@app.route('/posts', methods=['GET'])
def index_post():
    return render_template('post-index.html')
    # render post index page

@app.route('/posts', methods=['POST'])
def create_post():
    title = request.form.get('title', None)
    created_at = datetime.now()
    content = request.form.get('content', None)
    new_post = Post(title, created_at, content)
    try :
        dao.add(new_post)
        dao.commit()
        return redirect(url_for('read_post', post_id=new_post.id))
    except:
        return redirect(url_for('index'))

@app.route('/posts/new', methods=['GET'])
def new_post():
    return render_template('post-new.html')

@app.route('/posts/<int:post_id>', methods=['GET'])
def read_post(post_id):
    try:
        post = dao.query(Post).filter_by(id=post_id).one()
        # 이런 걸 모아서 util을 만들어도...
        return post
        # render post page
    except NoResultFound:
        abort(404);
    except MultipleResultsFound:
        abort(404);

@app.route('/posts/<int:post_id>/edit', methods=['GET'])
def edit_post(post_id):
    try :
        post = dao.query(Post).filter_by(id=post_id).one()
        return post
        # render post edit page
    except NoResultFound:
        abort(404);
    except MultipleResultsFound:
        abort(404);

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    try :
        post = dao.query(Post).filter_by(id=post_id).one()
        title = request.form.get('title', None)
        content = request.form.get('content', None)
        post.title = title
        post.content = content
        dao.commit()
        return redirect(url_for('read_post', post_id=post_id))
    except NoResultFound:
        abort(404);
    except MultipleResultsFound:
        abort(404);
    except:
        return redirect(url_for('index'))

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try :
        post = dao.query(Post).filter_by(id=post_id).one()
        dao.delete(post)
        dao.commit()
        return redirect(url_for('index'))
    except NoResultFound:
        abort(404);
    except MultipleResultsFound:
        abort(404);

@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    try:
        post = dao.query(Post).filter_by(id=post_id).one()
        name = request.form.get('name', None)
        created_at = datetime.now()
        content = request.form.get('content', None)
        ip = request.remote_addr
        new_comment = Comment(name, created_at, content, post_id, ip=ip)
        dao.add(new_comment)
        dao.commit()
        return redirect(url_for('read_post', post_id=post_id))
    except NoResultFound:
        abort(404);
    except MultipleResultsFound:
        abort(404);
    except:
        pass

@app.route('/posts/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(post_id, comment_id):
    try:
        comment = Comment.query.filter_by(id=comment_id).one()
        dao.delete(comment)
        dao.commit()
        return redirect(url_for('read_post', post_id=post_id))
    except NoResultFound:
        abort(404);
    except MultipleResultsFound:
        abort(404);
