import requests
import json

# API地址
API_URL = 'http://localhost:8001'

# 管理员用户数据
admin_data = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'adminpassword'
}

# 创建管理员用户
response = requests.post(
    f'{API_URL}/users/',
    headers={'Content-Type': 'application/json'},
    data=json.dumps(admin_data)
)

# 打印响应
print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')

# 如果创建成功，更新用户为管理员
if response.status_code == 200:
    user_id = response.json()['id']
    # 这里需要管理员权限才能更新用户角色
    # 我们可以直接修改数据库来设置管理员权限
    print('User created successfully. You need to set is_admin=True in the database.')
else:
    print('Failed to create admin user.')