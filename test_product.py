import os
import json
import unittest

class TestProduct(unittest.TestCase):
    def test_get_license_info(self):
        user_id = '12345'
        license_info = get_license_info(user_id)
        self.assertEqual(json.loads(license_info)['user_id'], user_id)
        self.assertEqual(json.loads(license_info)['status'], 'active')
        self.assertEqual(json.loads(license_info)['expiry_date'], '2023-12-31')

    def test_update_license_status(self):
        user_id = '12345'
        update_license_status(user_id, 'expired')
        self.assertEqual(get_license_info(user_id)['status'], 'expired')

if __name__ == '__main__':
    unittest.main()