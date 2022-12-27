import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gsolvit'

    @staticmethod
    def init_app(app):
        pass
# configuration of the database
config = {
    'default': Config,
    'MYSQL_PASSWORD': 'yourpassword',
    'DATABASE_NAME': 'test'
}
