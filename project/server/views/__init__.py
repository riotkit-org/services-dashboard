# project/server/main/__init__.py

from flask import Blueprint
from ..container import Container


class ContainerAwareBlueprint(Blueprint):
    container = None  # type: Container

    def register(self, app, options, first_registration=False):
        self.container = app
        super(ContainerAwareBlueprint, self).register(app, options, first_registration)
