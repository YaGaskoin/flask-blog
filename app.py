from flask import Flask, redirect, url_for
from config import Configuration
from models import db, migrate, Post, Tag, User, Role
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_object(Configuration)

db.init_app(app)
app.db = db
migrate.init_app(app, db)

mail = Mail(app)

class MicroBlog(ModelView):

    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, **kwargs):
        return redirect(url_for('index'))


admin = Admin(app)
admin.add_view(MicroBlog(Post, db.session))
admin.add_view(MicroBlog(Tag, db.session))
admin.add_view(MicroBlog(User, db.session))
admin.add_view(MicroBlog(Role, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


