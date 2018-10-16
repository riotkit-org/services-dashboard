# project/server/main/views.py


from flask import render_template, request
from . import ContainerAwareBlueprint
from ..service.security import AdminLoginChecker


main_blueprint = ContainerAwareBlueprint('main', __name__,)


@main_blueprint.route('/admin/<token>')
def admin_home(token: str):
    container = main_blueprint.container

    if not AdminLoginChecker.is_admin_token_valid(container.config, token):
        return render_template('errors/401.html'), 401

    return home(allow_admin_services=True)


@main_blueprint.route('/')
def home(allow_admin_services=False):
    container = main_blueprint.container
    provider = container.provider_factory.create(
        container.config['APP_PROVIDER'],
        container.config['APP_PROVIDER_URL']
    )

    enabled_services = provider.list_all_enabled_services(allow_admin_services=allow_admin_services)

    return render_template('main/home.html', services=enabled_services)
