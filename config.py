HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'tracker'
USERNAME = 'root'
PASSWORD = '142536'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?" \
         "charset=utf8".\
    format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT,
           db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
_static_folder = './static/'
add_template_global = './templates/css/'
SECRET_KEY = 'AKSKDJWI2IIIEIDK4111115524668'
BABEL_DEFAULT_LOCALE = 'zh_CN'
