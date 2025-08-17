class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATED_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    UPDATE_USER = '/api/auth/user'
    CREATED_ORDER = '/api/orders'
    GET_ORDERS_USER = '/api/orders'
    DELETE_USER = '/api/auth/user'

class Ingredients:
    BODY_WITHOUT_INGREDIENTS = { 'ingredients': []}
    BODY_INVALID_HASH_INGREDIENT = {'ingredients': ['61c0c5a71d1f82001bdaaa6c1']}

    @staticmethod
    def ingredients_body():
        bun = '61c0c5a71d1f82001bdaaa6c'
        main = '61c0c5a71d1f82001bdaaa6e'
        souse = '61c0c5a71d1f82001bdaaa73'
        return { 'ingredients': [bun, main, souse]}

class DataResponse:
    ORDER_WITHOUT_INGREDIENTS = {"success": False,"message": "Ingredient ids must be provided"}
    CREATING_REGISTERED_USER = {"success": False,"message": "User already exists"}
    CREATING_USER_WITHOUT_FILLED_FIELD = {"success": False, "message": "Email, password and name are required fields"}
    RECEIVING_ORDERS_AUTHORIZED_USER = {"success": False,"message": "You should be authorised"}
    AUTHORIZATION_WITH_INCORRECT_USERNAME_AND_PASSWORD = {"success": False,"message": "email or password are incorrect"}
    UPDATE_DATA_WITHOUT_AUTHORIZATION_USER = {"success": False,"message": "You should be authorised"}