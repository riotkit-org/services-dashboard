
import unittest

from base import BaseTestCase
from project.server.models import Service


class TestMetadataParser(BaseTestCase):
    def test_is_web_service(self):
        self.assertTrue(Service('iwa-ait.org', [80], 'test', {})
                        .is_web_service())

    def test_get_domain(self):
        self.assertEquals(
            'iwa-ait.org',
            Service('iwa-ait.org', [80], 'test', {}).get_domain()
        )

    def test_get_description(self):
        self.assertEquals(
            'Call against the eviction and destruction of the forest',
            Service('hambachforest.org', [80], 'test', {
                'DESCRIPTION': 'Call against the eviction and destruction of the forest'
            }).get_description()
        )

    def test_is_visible_only_for_admin(self):
        self.assertEquals(
            'Call against the eviction and destruction of the forest',
            Service('hambachforest.org', [80], 'test', {
                'DESCRIPTION': 'Call against the eviction and destruction of the forest'
            }).get_description()
        )

    def test_get_icon_default(self):
        self.assertEquals(
            'some-icon',
            Service('hambachforest.org', [80], 'test', {'ICON': 'some-icon'}).get_icon()
        )

    def test_get_icon_custom(self):
        self.assertEquals(
            'pe-7s-global',
            Service('hambachforest.org', [80], 'test', {}).get_icon()
        )

    def test_is_enabled(self):
        self.assertTrue(
            Service('hambachforest.org', [80], 'test', {
                'ENABLED': 'true'
            }).is_enabled()
        )

    def test_is_enabled_case_yes_word(self):
        self.assertTrue(
            Service('hambachforest.org', [80], 'test', {
                'ENABLED': 'yes'
            }).is_enabled()
        )

    def test_is_enabled_negative_case(self):
        self.assertFalse(
            Service('hambachforest.org', [80], 'test', {
                'ENABLED': 'false'
            }).is_enabled()
        )

    def test_get_discovery_type(self):
        self.assertEquals(
            'kubernetes',
            Service('kubernetes', [80], 'kubernetes', {}).get_discovery_type()
        )


if __name__ == '__main__':
    unittest.main()
