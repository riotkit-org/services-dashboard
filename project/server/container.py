
from flask import Flask
from .factory.providerfactory import ProviderFactory


class Container(Flask):
    provider_factory = None  # type: ProviderFactory
