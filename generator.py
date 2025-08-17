import random

class DataCreatedUser:

    @staticmethod
    def generate_body():
        return {"email": f'www9626-{random.randint(1000, 9999)}@yandex.ru',
                "password": f'{random.randint(100000, 999999)}a',
                "name": f'Valeria{random.randint(100, 999)}'
                }