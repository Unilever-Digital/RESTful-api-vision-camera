from flask import (
    Flask,
    session,
    url_for,
    render_template,
    Blueprint,
    redirect,
    request
)
import os
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    """ app init

    Args:
        test_config (_type_, optional): _description_. Defaults to None.

    Returns:
        app : Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    db = SQLAlchemy(app)
    db.create_all()
 
    from .views.view import blog
    app.register_blueprint(blog)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        app.config.from_mapping(SECRET_KEY='unilever_digital',
                                DATABASE=os.path.join(
                                app.instance_path, 'flaskr.sqlite'),
                                CACHE_TYPE='FileSystemCache',
                                CACHE_DIR='cache',
                                CACHE_THRESHOLD=100000,)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a base page
    @app.route('/')
    def main():
        return redirect(url_for('auth.home'))

    return app