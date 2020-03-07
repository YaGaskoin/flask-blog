class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost:5432/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ключ'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'danilacerncov@gmail.com'
    MAIL_DEFAULT_SENDER = 'danilacerncov@gmail.com'
    MAIL_PASSWORD = 'danilkaka'
