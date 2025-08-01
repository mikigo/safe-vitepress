import bcrypt
from tortoise import Tortoise, run_async

from backend.models.user import User

DB_CONFIG = {
    'connections': {
        'default': 'sqlite://db.sqlite3'
    },
    'apps': {
        'models': {
            'models': ['backend.models.user'],
            'default_connection': 'default',
        },
    }
}


async def create_admin(admin_username: str, admin_password: str):
    await Tortoise.init(config=DB_CONFIG)
    await Tortoise.generate_schemas()

    existing_admin = await User.filter(is_admin=True).first()
    if existing_admin:
        print('Admin user already exists.')
        return

    hashed_password = bcrypt.hashpw(admin_password.encode('utf-8'), bcrypt.gensalt())
    admin_user = await User.create(
        username=admin_username,
        email='admin@example.com',
        hashed_password=hashed_password.decode('utf-8'),
        is_admin=True
    )

    print(f'Admin user created successfully with ID: {admin_user.id}')


if __name__ == '__main__':
    admin_username = input('Enter admin username: ')
    admin_password = input('Enter admin password: ')
    check_password = input('Re-enter admin password: ')
    if admin_password != check_password:
        print('Passwords do not match. Exiting.')
        exit(1)
    run_async(create_admin(admin_username, admin_password))
