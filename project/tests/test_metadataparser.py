
import unittest

from base import BaseTestCase
from unittest_data_provider import data_provider
from project.server.service.metadataparser import MetadataParser


def container_data_provider():
    return (
        # empty data, no env variables, no labels
        (
            [],
            {},

            # nothing is parsed
            [], [], {}
        ),

        # env variables only, no any labels used
        (
            [
                'VIRTUAL_HOST=afed.org.uk',
                'VIRTUAL_PORT=8000',
                'DSD_ENABLED=true',
                'DSD_ONLY_FOR_ADMIN=false'
            ],
            {},
            ['afed.org.uk'], ['8000'], {
                'ENABLED': 'true',
                'ONLY_FOR_ADMIN': 'false'
            }
        ),

        # labels only
        (
            [],
            {
                'org.riotkit.dashboard.domain': 'federacja-anarchistyczna.pl',
                'org.riotkit.dashboard.enabled': 'true',
                'org.riotkit.dashboard.only_for_admin': 'false'
            },
            ['federacja-anarchistyczna.pl'], [80], {
                'ENABLED': 'true',
                'ONLY_FOR_ADMIN': 'false',
                'DOMAIN': 'federacja-anarchistyczna.pl'
            }
        ),

        # mixed labels and environment variables
        (
            [
                'LETSENCRYPT_HOST=hambachforest.org'
            ],
            {
                'org.docker.services.dashboard.enabled': 'true',
                'org.docker.services.dashboard.only_for_admin': 'false'
            },
            ['hambachforest.org'], [80], {
                'ENABLED': 'true',
                'ONLY_FOR_ADMIN': 'false'
            }
        ),

        # traefik support
        (
            [],
            {
                'traefik.frontend.rule': 'wolnywroclaw.pl',
                'org.docker.services.dashboard.enabled': 'true',
                'org.docker.services.dashboard.only_for_admin': 'false'
            },
            ['wolnywroclaw.pl'], [80], {
                'ENABLED': 'true',
                'ONLY_FOR_ADMIN': 'false'
            }
        ),
    )


class TestMetadataParser(BaseTestCase):
    @data_provider(container_data_provider)
    def test_parse(self,
                                           input_env: list,
                                           input_labels: dict,
                                           expected_domains: list,
                                           expected_ports: list,
                                           expected_attributes: dict):
        domains, ports, attributes = MetadataParser.parse(input_env, input_labels)
        self.assertEquals(expected_domains, list(domains))
        self.assertEquals(expected_ports, list(ports))
        self.assertEquals(expected_attributes, dict(attributes))


if __name__ == '__main__':
    unittest.main()
