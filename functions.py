from flask import request
from models import db, Post


def make_pagination(items_per_page, obj):
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    return obj.paginate(page=page, per_page=items_per_page)


def create_post():
    title = request.form.get('title')
    body = request.form.get('body')
    try:
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
    except Exception:
        print(Exception)


def check_search():
    q = request.args.get('q')
    if q:
        return Post.query.filter(Post.title.contains(q))
    else:
        return Post.query
