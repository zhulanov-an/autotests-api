from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Описание общей структуры пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class UserResponseSchema(UserSchema):
    """
    Описание структуры созданного пользователя.
    """
    id: str


class CreateUserRequestSchema(UserSchema):
    """
    Описание структуры запроса на создание пользователя.
    """
    password: str


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на создания пользователя.
    """
    user: UserResponseSchema
