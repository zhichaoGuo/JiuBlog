import os

from flask import Flask, render_template

from jiublog.blog.views import blog
from jiublog.config import config_dict
from jiublog.extension import db, bootstrap, login_manager
from jiublog.manager.views import manager


def create_app(config_name=None):
    app = Flask('jiublog')
    if config_name:
        app.config.from_object(config_dict[config_name.capitalize()])
    # app.jinja_env.filters['split'] = split_space  # 增加jinja2的过滤器函数
    register_extension(app)
    register_blueprint(app)
    configure_database(app)
    error_execute(app)
    return app


def register_extension(app):
    # migrate.init_app(app, db)
    db.init_app(app)
    db.app = app
    bootstrap.init_app(app)
    # moment.init_app(app)
    # ckeditor.init_app(app)
    login_manager.init_app(app)
    # share.init_app(app)
    # avatar.init_app(app)
    # mail.init_app(app)
    # mail.app = app
    # whooshee.init_app(app)
    # oauth.init_app(app)
    # babel.init_app(app)
    # cache.init_app(app, config={'CACHE_TYPE': 'redis'})


def register_blueprint(app):
    app.register_blueprint(blog)
    app.register_blueprint(manager)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        try:
            db.create_all()
        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e))
            # fallback to SQLite
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sqlite', 'db.sqlite3')
            print('> Fallback to SQLite ')
            db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def error_execute(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html'), 404

    @app.errorhandler(400)
    def bad_request(e):
        return render_template('error/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('error/403.html'), 403

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('error/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error/500.html'), 500

    # @app.errorhandler(CSRFError)
    # def handle_csrf_error(e):
    #     return render_template('error/400.html', description=e.description), 500
if __name__ == '__main__':
    app = create_app('production')
    app.run(port=5678)