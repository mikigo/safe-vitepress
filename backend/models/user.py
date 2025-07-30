import uuid

from passlib.context import CryptContext
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, editable=False)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    hashed_password = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)
    is_admin = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return pwd_context.hash(password)

    class Meta:
        table = "users"
        ordering = ["-created_at"]


User_Pydantic = pydantic_model_creator(User, name="User")
UserCreate_Pydantic = pydantic_model_creator(User, name="UserCreate", exclude_readonly=True,
                                             exclude=["is_active", "is_admin"])
UserUpdate_Pydantic = pydantic_model_creator(User, name="UserUpdate", exclude_readonly=True)
