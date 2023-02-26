import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Config(object):
    BLOG_THEMES = {'light': 'light', 'dark': 'dark'}
    # Paginate configure
    JiuBLOG_BLOG_PER_PAGE = 8
    JiuBLOG_COMMENT_PER_PAGE = 10
    JiuBLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    BLOG_PHOTO_PER_PAGE = 12
    LOGIN_LOG_PER_PAGE = 20
    SECRET_KEY = 'jiu_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DATABASE_USER = 'root'
    DATABASE_PWD = '8854218guo'
    # Photo Configure
    PHOTO_NEED_RESIZE = 1024 * 1024
    # DEFAULT AVATAR CONFIGURE
    AVATARS_SAVE_PATH = JiuBLOG_UPLOAD_PATH + '/avatars/'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@127.0.0.1/blog?charset=utf8mb4'.format(Config.DATABASE_USER,
                                                                                            Config.DATABASE_PWD)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@127.0.0.1/blog?charset=utf8mb4'.format(Config.DATABASE_USER,
                                                                                            Config.DATABASE_PWD)


config_dict = {
    'Development': DevelopmentConfig,
    'Production': ProductionConfig
}
