from data import DataResponse
from user_methods import UserMethods
import allure

class TestLoginUser: # Логин пользователя

    @allure.title('Авторизация под существующем пользователем')
    def test_login_existing_user(self, creating_user):
        token, user_body = creating_user
        login_body = {"email": user_body["email"], "password": user_body["password"]}
        response = UserMethods.login_user(login_body)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Авторизация с неверным логином и паролем')
    def test_authorization_with_incorrect_username_and_password(self, creating_user):
        token, user_body = creating_user
        login_body = {"email": f'q{user_body["email"]}', "password": f'5{user_body["password"]}'}
        response = UserMethods.login_user(login_body)
        expected_body = DataResponse.AUTHORIZATION_WITH_INCORRECT_USERNAME_AND_PASSWORD
        actual_body = response.json()

        assert response.status_code == 401
        assert actual_body == expected_body