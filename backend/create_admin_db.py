from tortoise import Tortoise, run_async
from backend.models.user import User
import bcrypt

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
    await Tortoise.init(config=DB_CONFIG)
    await Tortoise.generate_schemas()

    existing_admin = await User.filter(is_admin=True).first()
    if existing_admin:
        print('Admin user already exists.')
        return

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