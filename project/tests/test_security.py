
import unittest

from base import BaseTestCase
from project.server.service.security import AdminLoginChecker
from flask import Config


class TestMetadataParser(BaseTestCase):
    def test_is_admin_token_valid(self):
        app_config = Config({})
        app_config['APP_ADMIN_TOKEN'] = 'test'

        self.assertTrue(AdminLoginChecker.is_admin_token_valid(app_config, 'test'))
        self.assertFalse(AdminLoginChecker.is_admin_token_valid(app_config, '1234'))


if __name__ == '__main__':
    unittest.main()
