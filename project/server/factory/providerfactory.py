
from ..provider.docker import DockerServicesProvider
from ..provider.test import TestServicesProvider
from ..provider import ServiceProvider


class ProviderFactory:
    """ Create a proper data-provider instance basing on the configuration """

    mapping = {
        'docker': DockerServicesProvider,
        'test': TestServicesProvider
    }

    def create(self, name: str, url: str) -> ServiceProvider:
        """ Creates the provider instance """

        if name not in self.mapping:
            raise Exception('Invalid APP_PROVIDER, possible values: ' + str(self.mapping.keys()))

        return self.mapping[name](url)
