from flask import render_template, request, redirect
from app import app, user_datastore
from models import Post, Tag, db, User
from functions import make_pagination, create_post, check_search
from flask_security import login_required, logout_user, login_user, current_user
from flask_security.utils import hash_password


@app.route('/')
def index():
    posts = check_search()
    pages = make_pagination(5, posts)
    return render_template('index.html', posts=posts, pages=pages)


@app.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('post.html', post=post, tags=tags)


@app.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts
    return render_template('tag.html', tag=tag, posts=posts)


@app.route('/create/', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        create_post()
    return render_template('create.html')


@app.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if request.method == 'POST':
        body = request.form.get('body')
        Post.query.filter(Post.slug == slug).update({'body': body})
        db.session.commit()

    return render_template('edit_post.html', post=post)


@app.route('/logout')
def logout():
    logout_user()
    redirect(index)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        if not User.query.filter(User.email == request.form.get('email')).first():
            user_datastore.create_user(email=request.form.get('email'),
                                       password=hash_password(request.form.get('password')))
            db.session.commit()
            user = User.query.filter(User.email == request.form.get('email')).first()
            login_user(user)
            return redirect('/')
    return render_template('registration.html')







