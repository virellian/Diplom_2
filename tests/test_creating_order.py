import allure
from data import Ingredients, DataResponse
from order_methods import OrderMethods


class TestCreatingOrder: # Создание заказа

    @allure.title('Успешное создание заказа')
    def test_successful_creating_order(self, creating_user):
        token, user_body = creating_user
        order_body = Ingredients.ingredients_body()
        response = OrderMethods.created_order(order_body, token )
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создания заказа без авторизации')
    def test_error_creating_order_without_authorization(self, creating_user):
        token = ''
        order_body = Ingredients.ingredients_body()
        response = OrderMethods.created_order(order_body, token)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_creating_order_without_ingredients(self, creating_user):
        token, user_body = creating_user
        order_body = Ingredients.BODY_WITHOUT_INGREDIENTS
        response = OrderMethods.created_order(order_body, token)
        actual_body = response.json()
        expected_body = DataResponse.ORDER_WITHOUT_INGREDIENTS

        assert response.status_code == 400
        assert actual_body == expected_body

    @allure.title('Создание заказа с невалидным хешом ингредиента')
    def test_creating_order_with_invalid_hash_ingredient(self, creating_user):
        token, user_body = creating_user
        order_body = Ingredients.BODY_INVALID_HASH_INGREDIENT
        response = OrderMethods.created_order(order_body, token)

        assert response.status_code == 500