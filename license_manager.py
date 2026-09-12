import os
import json

def get_license_info(user_id):
    # Simulate fetching license information from a database
    license_info = {'user_id': user_id, 'status': 'active', 'expiry_date': '2023-12-31'}
    return json.dumps(license_info)

def update_license_status(user_id, status):
    # Simulate updating license status in a database
    print(f'Updated license status for user {user_id} to {status}')

if __name__ == '__main__':
    user_id = '12345'
    license_info = get_license_info(user_id)
    print(license_info)
    update_license_status(user_id, 'expired')