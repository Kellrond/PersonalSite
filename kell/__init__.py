import os
from flask              import Flask


def create_app(test_config=None, instance_relative_config=True):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = b'0fb1859ab065c1ce477ddcc5ad1aab39b9d6a972c1cc6e97889316cc4d333968',
        DATABASE = os.path.join(app.instance_path, 'kell.sqlite'),
    )

    print(app.instance_path)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .logic import schema as dbo
    dbo.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

