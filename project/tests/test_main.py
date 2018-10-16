# project/server/tests/test_main.py


import unittest

from base import BaseTestCase


class TestMainBlueprint(BaseTestCase):

    def test_index(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'for Anarchist movement purpose', response.data)
        self.assertNotIn(b'admin.iwa-ait.org', response.data)  # admin-only service should not appear there

    def test_default_configured_admin_endpoint(self):
        response = self.client.get('/admin/YOUR-SECRET-ADMIN-KEY', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'for Anarchist movement purpose', response.data)

        # example services
        self.assertIn(b'solfed.org.uk', response.data)
        self.assertIn(b'iwa-ait.org', response.data)
        self.assertIn(b'admin.iwa-ait.org', response.data)  # admin-only service should be present

    def test_invalid_admin_password(self):
        response = self.client.get('/admin/invalid-password', follow_redirects=True)
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
