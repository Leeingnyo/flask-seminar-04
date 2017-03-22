from flask import render_template, request, redirect, url_for, abort
from blog import app

@app.route('/posts', methods=['GET'])
def index_post():
    return '글 페이지'

@app.route('/posts', methods=['POST'])
def create_post():
    return '새 글'

@app.route('/posts/<int:post_id>', methods=['GET'])
def read_post():
    return '글 하나'

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post():
    return '글 수정'

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post():
   return '글 삭제' 

@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def read_comments():
    return '댓글 작성'

@app.route('/posts/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment():
    return '댓글 삭제'
