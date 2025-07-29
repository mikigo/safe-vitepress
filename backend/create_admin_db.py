from tortoise import Tortoise, run_async
from models.user import User
import bcrypt

# 数据库配置
DB_CONFIG = {
    'connections': {
        'default': 'sqlite://db.sqlite3'
    },
    'apps': {
        'models': {
            'models': ['models.user'],
            'default_connection': 'default',
        },
    }
}

async def create_admin():
    # 初始化Tortoise ORM
    await Tortoise.init(config=DB_CONFIG)
    await Tortoise.generate_schemas()

    # 检查是否已存在管理员用户
    existing_admin = await User.filter(is_admin=True).first()
    if existing_admin:
        print('Admin user already exists.')
        return

    # 创建管理员用户
    hashed_password = bcrypt.hashpw('adminpassword'.encode('utf-8'), bcrypt.gensalt())
    admin_user = await User.create(
        username='admin',
        email='admin@example.com',
        hashed_password=hashed_password.decode('utf-8'),
        is_admin=True
    )

    print(f'Admin user created successfully with ID: {admin_user.id}')

if __name__ == '__main__':
    run_async(create_admin())