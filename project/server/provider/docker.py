
import docker

from . import ServiceProvider
from ..models import Service
from ..service.metadataparser import MetadataParser


class DockerServicesProvider(ServiceProvider):
    docker_address = ''
    client = None  # type: docker.DockerClient

    def __init__(self, url):
        self.docker_address = url
        self.client = docker.DockerClient(base_url=url)

    def list_all_enabled_services(self, allow_admin_services: bool) -> list:
        enabled = list(filter(lambda c: c.is_enabled(), self._parse_containers_list()))

        if not allow_admin_services:
            return list(filter(lambda c: not c.is_visible_only_for_admin(), enabled))

        return enabled

    def _parse_containers_list(self) -> list:
        containers = self.client.containers.list()
        services = list()

        for container in containers:
            domains, ports, attributes = MetadataParser.parse(
                container.attrs['Config']['Env'],
                container.labels
            )

            for domain in domains:
                services.append(Service(domain, ports, 'docker', attributes))

        return services

