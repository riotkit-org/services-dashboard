
from . import ServiceProvider
from ..models import Service


class TestServicesProvider(ServiceProvider):

    def __init__(self, url):
        pass

    def list_all_enabled_services(self, allow_admin_services: bool) -> list:
        enabled = list(filter(lambda c: c.is_enabled(), self._parse_containers_list()))

        if not allow_admin_services:
            return list(filter(lambda c: not c.is_visible_only_for_admin(), enabled))

        return enabled

    def _parse_containers_list(self) -> list:
        return [
            Service('iwa-ait.org', [80, 443], 'test', {
                'DESCRIPTION': 'International Workers Association home page',
                'ENABLED': 'true'
            }),
            Service('zsp.net.pl', [443, 80], 'test', {
                'DESCRIPTION': 'Syndicalist Union of Poland a section of IWA-AIT, helps all type of workers,'
                               ' including temporary workers and civil-contract workers',
                'ENABLED': 'true'
            }),
            Service('solfed.org.uk', [443, 80], 'test', {
                'DESCRIPTION': 'Solidarity Federation, helping with workers and tenants rights',
                'ENABLED': 'true'
            }),
            Service('priamaakcia.sk', [443, 80], 'test', {
                'DESCRIPTION': 'Priama Akcia',
                'ENABLED': 'true'
            }),
            Service('admin.iwa-ait.org', [5000, 80], 'test', {
                'DESCRIPTION': 'Some administration page',
                'ENABLED': 'true',
                'ONLY_FOR_ADMIN': 'true'
            })
        ]
