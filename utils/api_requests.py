import requests
import allure
from utils.links import Links


class APIRequests:
    BASE_URL = Links.BASE_URL

    @allure.step("Создание пользователя")
    def create_user(self, email, password, name):
        payload = {'email': email, 'password': password, 'name': name}
        response = requests.post(f"{self.BASE_URL}{Links.REGISTER}", json=payload)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.delete(f"{self.BASE_URL}{Links.USER}", headers=headers)
        return response
