import requests
import json

API_URL = 'http://localhost:8000'

admin_data = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'adminpassword'
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