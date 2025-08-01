from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import register_tortoise
import os
from datetime import timedelta
from backend.auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, Token, get_current_active_user
from backend.models.user import User, User_Pydantic, UserCreate_Pydantic

app = FastAPI(title="Safe Vitepress Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TORTOISE_ORM = {
    "connections": {
        "default": os.getenv("DATABASE_URL", "sqlite://./db.sqlite3")
    },
    "apps": {
        "models": {
            "models": ["backend.models.user", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def read_root():
    return {"message": "Welcome to Vitepress Auth Backend"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(username=form_data.username)
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=User_Pydantic)
async def read_users_me(current_user: User_Pydantic = Depends(get_current_active_user)):
    """获取当前登录用户信息"""
    return current_user


async def get_current_admin_user(current_user: User_Pydantic = Depends(get_current_active_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user


@app.post("/users/", response_model=User_Pydantic)
async def create_user(user: UserCreate_Pydantic, admin_user: User_Pydantic = Depends(get_current_admin_user)):
    if await User.filter(username=user.username).exists():
        raise HTTPException(status_code=400, detail="Username already registered")
    if await User.filter(email=user.email).exists():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = User.get_password_hash(user.password)
    user_obj = await User.create(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    return await User_Pydantic.from_tortoise_orm(user_obj)
