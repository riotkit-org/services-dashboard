# project/server/__init__.py


import os

from flask import render_template
from flask_debugtoolbar import DebugToolbarExtension

from .factory.providerfactory import ProviderFactory
from .container import Container as Flask


# instantiate the extensions
toolbar = DebugToolbarExtension()


def create_app(script_info=None, debug=True):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder='../client/templates',
        static_folder='../client/static'
    )

    # set config
    app_settings = os.getenv(
        'APP_SETTINGS',
        'project.server.config.DevelopmentConfig'
    )

    app.config.from_object(app_settings)
    pass_configuration_from_env(app)

    # set up extensions
    if debug:
        toolbar.init_app(app)

    # bootstrap.init_app(app)

    # register blueprints
    from project.server.views.home import main_blueprint
    app.register_blueprint(main_blueprint)
    app.provider_factory = ProviderFactory()

    # error handlers
    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template('errors/401.html'), 401

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app


def pass_configuration_from_env(app: Flask):
    allowed = {
        'APP_PROVIDER': 'docker',
        'APP_PROVIDER_URL': 'unix:///var/run/docker.sock',
        'APP_ADMIN_TOKEN': 'YOUR-SECRET-ADMIN-KEY',
        'APP_NAME': None
    }

    for key, value in allowed.items():
        env_value = os.getenv(key, value)

        if not env_value and value is None:
            continue

        app.config[key] = env_value
