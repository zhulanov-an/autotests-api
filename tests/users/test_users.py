from http import HTTPStatus

import allure
import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
class TestUsers:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    def test_create_user(self, domain: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get user me")
    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):
        get_me_response = private_users_client.get_user_me_api()

        assert_status_code(get_me_response.status_code, HTTPStatus.OK)
        get_me_response_data = GetUserResponseSchema.model_validate_json(get_me_response.text)
        validate_json_schema(get_me_response.json(), get_me_response_data.model_json_schema())
        assert_get_user_response(get_me_response_data, function_user.response)
