class Config(object):
    BLOG_THEMES = {'light': 'light', 'dark': 'dark'}
    # Paginate configure
    JiuBLOG_BLOG_PER_PAGE = 8
    JiuBLOG_COMMENT_PER_PAGE = 10
    BLOG_PHOTO_PER_PAGE = 12
    LOGIN_LOG_PER_PAGE = 20
    SECRET_KEY = 'jiu_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DATABASE_USER='root'
    DATABASE_PWD='8854218guo'
    # Photo Configure
    PHOTO_NEED_RESIZE = 1024 * 1024


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
