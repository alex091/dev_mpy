import unittest

ADMIN_USER = "vasja.pupkin"
ADMIN_PASSWD = "passsecret"


def valid_admin_user(username, password):
    return username.lower() == ADMIN_USER and password == ADMIN_PASSWD


class AdminTestCase(unittest.TestCase):
    def test_valid_admin_user(self):
        self.assertTrue(valid_admin_user('vasja.pupkin', 'passsecret'))

    def test_invalid_admin_user(self):
        self.assertFalse(valid_admin_user('vasja.pupk', 'passret'))

    def test_incorrect_admin_password(self):
        self.assertFalse(valid_admin_user('vasja.pupk', 'passret'))

    def test_incorrect_admin_username(self):
        self.assertFalse(valid_admin_user('vasja.pupkin', 'passsret'))

    def test_empty_data(self):
        self.assertFalse(valid_admin_user('', ''))

    def test_empty_username(self):
        self.assertFalse(valid_admin_user('', 'passsret'))

    def test_empty_password(self):
        self.assertFalse(valid_admin_user('vasja.pupkin', ''))


if __name__ == '__main__':
    unittest.main()
