import json

import requests

def create_admin_user(admin_username: str, admin_password: str):

    API_URL = 'http://localhost:8000'

    admin_data = {
        'username': admin_username,
        'email': 'admin@example.com',
        'password': admin_password
    }

    response = requests.post(
        f'{API_URL}/users/',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(admin_data)
    )

    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

    if response.status_code == 200:
        user_id = response.json()['id']
        print('User created successfully. You need to set is_admin=True in the database.')
    else:
        print('Failed to create admin user.')

if __name__ == '__main__':
    admin_username = input('Enter admin username: ')
    admin_password = input('Enter admin password: ')
    check_password = input('Re-enter admin password: ')
    if admin_password != check_password:
        print('Passwords do not match. Exiting.')
        exit(1)
    create_admin_user(admin_username, admin_password)
