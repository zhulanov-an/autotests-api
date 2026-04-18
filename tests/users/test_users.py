from http import HTTPStatus

import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.parametrize(  # параметризация доменов электронной почты
    "domain",
    [
        "mail.ru",
        "gmail.com",
        "example.com"
    ]
)
def test_create_user(domain: str, public_users_client: PublicUsersClient):
    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema(email=fake.email(domain=domain))
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)

    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем, что данные ответа совпадают с данными запроса
    assert_create_user_response(request, response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.users  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient):
    get_me_response = private_users_client.get_user_me_api()

    assert_status_code(get_me_response.status_code, HTTPStatus.OK)
    get_me_response_data = GetUserResponseSchema.model_validate_json(get_me_response.text)
    validate_json_schema(get_me_response.json(), get_me_response_data.model_json_schema())
    assert_get_user_response(get_me_response_data, function_user.response)
