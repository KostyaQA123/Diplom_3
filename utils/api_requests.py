import requests
import allure
import json
from utils.links import Links


class APIRequests:
    BASE_URL = Links.BASE_URL

    def create_user(self, email, password, name):
        endpoint = Links.REGISTER
        with allure.step(f"POST {self.BASE_URL}{endpoint}"):
            payload = {'email': email, 'password': password, 'name': name}
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=payload)
            allure.attach(json.dumps(payload), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def delete_user(self, access_token):
        endpoint = Links.USER
        with allure.step(f"DELETE {self.BASE_URL}{endpoint}"):
            headers = {'Authorization': f'Bearer {access_token}'}
            response = requests.delete(f"{self.BASE_URL}{endpoint}", headers=headers)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response
